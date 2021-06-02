from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth import login, logout

# def home(request):
#     return render(request, 'pages/home.html')

def register(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'],first_name=request.POST['firstname'],last_name=request.POST['lastname'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render(request, 'accounts/register.html',{'error':'Password must match'})

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html',{'error':'Username or Password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def createuserprofile(request):
    if request.method == 'GET':
        return render(request, 'accounts/createuserprofile.html', {'form':UserProfileForm()})
    else :
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('index')
        return render(request, 'accounts/createuserprofile.html', {'form':UserProfileForm(), 'error':'Bad data'})


def viewuserprofile(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    if request.method == 'GET':
        form = UserProfileForm(instance=profile)
        return render(request, 'accounts/viewuserprofile.html',{'profile':profile, 'form':form})
    else:
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewuserprofile')
        return render(request, 'finance/updatesale.html', {'form':Salesform(), 'error':'Bad data'})

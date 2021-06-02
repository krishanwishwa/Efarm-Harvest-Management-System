from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from .forms import Blogform
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import requests
import datetime

def bloghome(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/bloghome.html', {'blogs':blogs})

def blogdetail(request,blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetail.html',{'blog':detailblog})

@login_required
def blogadd(request):
    if request.method == 'GET':
        return render(request, 'blog/blogadd.html', {'form':Blogform()})
    else :
        form = Blogform(request.POST,request.FILES or None)
        if form.is_valid():
            newblog = form.save(commit=False)
            newblog.auth = request.user
            newblog.save()
            return redirect('index')
        return render(request, 'blog/blogadd.html', {'form':Blogform(), 'error':'Bad data'})

#blog author view
def viewauthorprofile(request):
    profile = get_object_or_404(UserProfile,user=request.user)
    if request.method == 'GET':
        form = UserProfileForm(instance=profile)
        return render(request, 'blog/viewauthorprofile.html',{'profile':profile, 'form':form})
    else:
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewuserprofile')
        return render(request, 'finance/updatesale.html', {'form':Salesform(), 'error':'Bad data'})


def userblog(request):
    return render(request, 'blog/userblog.html')

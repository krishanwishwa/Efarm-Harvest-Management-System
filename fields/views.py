from django.shortcuts import render,redirect,get_object_or_404
from .models import Fields
from .forms import Fieldsform
from django.utils import timezone

def addfields(request):
    if request.method == 'GET':
        return render(request, 'fields/addfields.html', {'form':Fieldsform()})
    else :
        form = Fieldsform(request.POST,request.FILES or None)
        if form.is_valid():
            newfield = form.save(commit=False)
            newfield.user = request.user
            newfield.save()
            return redirect('viewfields')
        return render(request, 'fields/addfields.html', {'form':Fieldsform(), 'error':'Bad data'})

def viewfields(request):
    field = Fields.objects.filter(user=request.user)
    return render(request, 'fields/viewfields.html',{'field':field})

def map(request,f_id):
    f = get_object_or_404(Fields,pk=f_id,user=request.user)
    return render(request, 'fields/map.html',{'f':f})

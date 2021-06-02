from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Workers
from .models import Machines
from .forms import Workersform
from .forms import Machinesform
from django.utils import timezone

# employee add function
def addworkers(request):
    if request.method == 'GET':
        return render(request, 'resources/addworkers.html', {'form':Workersform()})
    else :
        form = Workersform(request.POST,request.FILES or None)
        if form.is_valid():
            newworker = form.save(commit=False)
            newworker.user = request.user
            newworker.save()
            return redirect('employeedetails')
        return render(request, 'resources/addworkers1.html', {'form':Workersform(), 'error':'Bad data'})

# employee view function
def employeedetails(request):
    employee = Workers.objects.filter(user=request.user)
    return render(request, 'resources/employeedetails.html',{'employee':employee})

# update employee
def updateemployee(request, employee_pk):
    emp = get_object_or_404(Workers, pk=employee_pk, user=request.user)
    if request.method == 'GET':
        form = Workersform(instance=emp)
        return render(request, 'resources/updateemployee.html',{'emp':emp, 'form':form})
    else:
        form = Workersform(request.POST, instance=emp)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('employeedetails')
        return render(request, 'resources/updateemployee.html', {'form':Workersform(), 'error':'Bad data'})

# machines add function
def addmachines(request):
    if request.method == 'GET':
        return render(request, 'resources/addmachines.html', {'form':Machinesform()})
    else :
        form = Machinesform(request.POST,request.FILES or None)
        if form.is_valid():
            newmachine = form.save(commit=False)
            newmachine.user = request.user
            newmachine.save()
            return redirect('machinedetails')
        return render(request, 'resources/addmachines.html', {'form':Machinesform(), 'error':'Bad data'})

# machines view function
def machinedetails(request):
    machine = Machines.objects.filter(user=request.user)
    return render(request, 'resources/machinedetails.html',{'machine':machine})

def updatemachine(request, machine_pk):
    mac = get_object_or_404(Machines, pk=machine_pk, user=request.user)
    if request.method == 'GET':
        form = Machinesform(instance=mac)
        return render(request, 'resources/updatemachine.html',{'mac':mac, 'form':form})
    else:
        form = Machinesform(request.POST, instance=mac)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('machinedetails')
        return render(request, 'resources/updatemachine.html', {'form':Machinesform(), 'error':'Bad data'})

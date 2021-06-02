from django.shortcuts import render,redirect,get_object_or_404
from .models import Sales
from .forms import Salesform
from .models import Expenses
from .forms import Expenseform
from django.utils import timezone

import requests
import datetime

# add sales
def addsale(request):
    if request.method == 'GET':
        return render(request, 'finance/addsale.html', {'form':Salesform()})
    else :
        form = Salesform(request.POST,request.FILES or None)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewsales')
        return render(request, 'finance/addsale.html', {'form':Salesform(), 'error':'Bad data'})

# sales view
def viewsales(request):
    sale = Sales.objects.filter(user=request.user)
    return render(request, 'finance/viewsales.html',{'sale':sale})

# sales update
def updatesales(request, sales_pk):
    s = get_object_or_404(Sales, pk=sales_pk, user=request.user)
    if request.method == 'GET':
        form = Salesform(instance=s)
        return render(request, 'finance/updatesale.html',{'s':s, 'form':form})
    else:
        form = Salesform(request.POST, instance=s)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewsales')
        return render(request, 'finance/updatesale.html', {'form':Salesform(), 'error':'Bad data'})

# delete sales
def deletesales(request, sales_pk):
    s = get_object_or_404(Sales, pk=sales_pk, user=request.user)
    if request.method == 'POST':
        s.delete()
        return redirect('viewsales')

# add Expenses
def addexpense(request):
    if request.method == 'GET':
        return render(request, 'finance/addexpense.html', {'form':Expenseform()})
    else :
        form = Expenseform(request.POST,request.FILES or None)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewexpenses')
        return render(request, 'finance/addexpense.html', {'form':Expenseform(), 'error':'Bad data'})

# view Expenses
def viewexpenses(request):
    expense = Expenses.objects.filter(user=request.user)
    return render(request, 'finance/viewexpenses.html',{'expense':expense})

def updateexpenses(request, expense_pk):
    e = get_object_or_404(Expenses, pk=expense_pk, user=request.user)
    if request.method == 'GET':
        form = Expenseform(instance=e)
        return render(request, 'finance/updateexpenses.html',{'e':e, 'form':form})
    else:
        form = Expenseform(request.POST, instance=e)
        if form.is_valid():
            newsale = form.save(commit=False)
            newsale.user = request.user
            newsale.save()
            return redirect('viewexpenses')
        return render(request, 'finance/updateexpenses.html', {'form':Expenseform(), 'error':'Bad data'})

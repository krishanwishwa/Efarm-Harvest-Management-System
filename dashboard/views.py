from django.shortcuts import render,redirect, get_object_or_404
from .models import Todo
from resources.models import Workers
from resources.models import Machines
from finance.models import Sales
from finance.models import Expenses
from fields.models import Fields
from .forms import TodoForm
from django.utils import timezone

import requests
import datetime
from datetime import datetime

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'dashboard/createtodo.html', {'form':TodoForm()})
    else :
        form = TodoForm(request.POST)
        if form.is_valid():
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodo')
        return render(request, 'dashboard/createtodo.html', {'form':TodoForm(), 'error':'Bad data'})

def currenttodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'dashboard/currenttodo.html',{'todos':todos})

def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'dashboard/todo.html',{'todo':todo, 'form':form})
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('currenttodo')
        return render(request, 'dashboard/todo.html', {'todo':todo, 'form':form, 'error':'Bad data'})

def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodo')

def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodo')

# dashboard apps data render function
def index(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    employee = Workers.objects.count()
    machine = Machines.objects.count()
    sale = Sales.objects.count()
    expense = Expenses.objects.count()
    field = Fields.objects.count()
    today = datetime.now()

    #chart
    this_year_jan = Sales.objects.filter(date__year=today.year,date__month=1).count()
    this_year_feb = Sales.objects.filter(date__year=today.year,date__month=2).count()
    this_year_mar = Sales.objects.filter(date__year=today.year,date__month=3).count()
    this_year_apr = Sales.objects.filter(date__year=today.year,date__month=4).count()
    this_year_may = Sales.objects.filter(date__year=today.year,date__month=5).count()
    this_year_jun = Sales.objects.filter(date__year=today.year,date__month=6).count()
    this_year_jul = Sales.objects.filter(date__year=today.year,date__month=7).count()
    this_year_aug = Sales.objects.filter(date__year=today.year,date__month=8).count()
    this_year_sep = Sales.objects.filter(date__year=today.year,date__month=9).count()
    this_year_oct = Sales.objects.filter(date__year=today.year,date__month=10).count()
    this_year_nov = Sales.objects.filter(date__year=today.year,date__month=11).count()
    this_year_dec = Sales.objects.filter(date__year=today.year,date__month=12).count()

    #daily weather data from API
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dc5ed03438df8d7350e3b34214437bb8'

    # city
    city = 'Colombo'
    # request the API data
    city_weather = requests.get(url.format(city)).json()

    #daily weather data
    weather = {
    'city': city,
    'temperature': city_weather['main']['temp'],
    'description': city_weather['weather'][0]['description'],
    'main': city_weather['weather'][0]['main'],
    'icon': city_weather['weather'][0]['icon'],
    'temperature_max': city_weather['main']['temp_max'] ,
    'temperature_min':  city_weather['main']['temp_min']  ,
    'feelslike_weather': city_weather['main']['feels_like'],
    'humidity': city_weather['main']['humidity'],
    'wind': city_weather['wind']['speed'],
    'country': city_weather['sys']['country'],

    }


    context = {
    'weather': weather,
    'todos': todos,
    'machine' : machine,
    'employee': employee,
    'sale': sale,
    'expense': expense,
    'field': field,
    'this_year_jan':this_year_jan,
    'this_year_feb':this_year_feb,
    'this_year_mar':this_year_mar,
    'this_year_apr':this_year_apr,
    'this_year_may':this_year_may,
    'this_year_jun':this_year_jun,
    'this_year_jul':this_year_jul,
    'this_year_aug':this_year_aug,
    'this_year_sep':this_year_sep,
    'this_year_oct':this_year_oct,
    'this_year_nov':this_year_nov,
    'this_year_dec':this_year_dec,
    'today':today,
    }
    return render(request, 'dashboard/index.html',context)


def home(request):
    return render(request, 'pages/home.html')

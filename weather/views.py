from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .forms import SearchForm

import requests
import datetime
# Create your views here.

#colombo weather page
@login_required
def colombo(request):
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
    'weather':weather
    }
    return render(request,'weather/colombo.html', context)

    # weather app for dashboard


def forecast(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&&units=metric&appid=dc5ed03438df8d7350e3b34214437bb8'

    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
    else:
        lat = 6.9271
        lon = 79.8612

    r = requests.get(url.format(lat,lon)).json()

    city_weather = {
        'temperature' : r['main']['temp'],
        'windspeed' : r['wind']['speed'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
        'temperature_max': r['main']['temp_max'] ,
        'humidity': r['main']['humidity'],
        'wind': r['wind']['speed'],
        'temperature_min':  r['main']['temp_min']  ,
        'feelslike_weather': r['main']['feels_like']
    }



        #forcasted weather data API
    v = 'http://api.openweathermap.org/data/2.5/forecast?q={}&&units=metric&appid=dc5ed03438df8d7350e3b34214437bb8'
    city = 'colombo'
    a = v.format(city)
    #accessing the API json data
    full = requests.get(a).json()

    # today's date taking as int
    day = datetime.datetime.today()
    today_date = int(day.strftime('%d'))


    forcast_data_list = {}


    for c in range(0, full['cnt']):
        date_var1 = full['list'][c]['dt_txt']
        date_time_obj1 = datetime.datetime.strptime(date_var1, '%Y-%m-%d %H:%M:%S')

        if int(date_time_obj1.strftime('%d')) == today_date or int(date_time_obj1.strftime('%d')) == today_date+1:

            if int(date_time_obj1.strftime('%d')) == today_date+1:
                today_date += 1
            forcast_data_list[today_date] = {}
            forcast_data_list[today_date]['day'] = date_time_obj1.strftime('%A')
            forcast_data_list[today_date]['date'] = date_time_obj1.strftime('%d %b, %Y')
            forcast_data_list[today_date]['time'] = date_time_obj1.strftime('%I:%M %p')
            forcast_data_list[today_date]['FeelsLike'] = full['list'][c]['main']['feels_like']

            forcast_data_list[today_date]['temperature'] = full['list'][c]['main']['temp']
            forcast_data_list[today_date]['temperature_max'] = full['list'][c]['main']['temp_max']
            forcast_data_list[today_date]['temperature_min'] = full['list'][c]['main']['temp_min']

            forcast_data_list[today_date]['description'] = full['list'][c]['weather'][0]['description']
            forcast_data_list[today_date]['icon'] = full['list'][c]['weather'][0]['icon']

            today_date += 1
        else:
            pass

    context = {
        'weather': city_weather, 'forcast_data_list':forcast_data_list
    }


    return render(request,'weather/forecast.html', context)

from django.urls import path,include
from . import views


urlpatterns = [

    path('colombo',views.colombo, name = 'colombo'),
    path('forecast',views.forecast, name = 'forecast'),

]

from django.urls import path,include
from . import views


urlpatterns = [
    path('addfields', views.addfields, name='addfields'),
    path('viewfields', views.viewfields, name='viewfields'),
    path('map/<int:f_id>', views.map, name='map'),

]

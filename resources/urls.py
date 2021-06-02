from django.urls import path,include
from . import views


urlpatterns = [

    path('addworkers', views.addworkers, name='addworkers'),
    path('employeedetails', views.employeedetails, name='employeedetails'),
    path('employee/<int:employee_pk>', views.updateemployee, name='updateemployee'),
    path('addmachines', views.addmachines, name='addmachines'),
    path('machinedetails', views.machinedetails, name='machinedetails'),
    path('machine/<int:machine_pk>', views.updatemachine, name='updatemachine'),

]

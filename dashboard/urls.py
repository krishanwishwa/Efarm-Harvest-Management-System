from django.urls import path,include
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('currenttodo/', views.currenttodo, name='currenttodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]

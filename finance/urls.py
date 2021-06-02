from django.urls import path,include
from . import views


urlpatterns = [
    path('addsale', views.addsale, name='addsale'),
    path('viewsales', views.viewsales, name='viewsales'),
    path('sales/<int:sales_pk>', views.updatesales, name='updatesales'),
    path('viewsales/<int:sales_pk>/delete', views.deletesales, name='deletesales'),
    path('addexpense', views.addexpense, name='addexpense'),
    path('viewexpenses', views.viewexpenses, name='viewexpenses'),
    path('expense/<int:expense_pk>', views.updateexpenses, name='updateexpenses'),
]

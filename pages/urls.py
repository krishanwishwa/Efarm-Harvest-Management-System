from django.urls import path,include
from . import views


urlpatterns = [

    path('product', views.product, name='product'),
    path('product/<int:product_id>/', views.productdetail, name='productdetail'),
    path('contact', views.contact, name='contact'),
    path('addproduct', views.addproduct, name='addproduct'),

]

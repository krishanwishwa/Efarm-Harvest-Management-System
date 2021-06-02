from django.urls import path,include
from . import views


urlpatterns = [

    path('carrotpricepredict', views.carrotpricepredict, name='carrotpricepredict'),
    path('potatopricepredict', views.potatopricepredict, name='potatopricepredict'),

]

from django.urls import path,include
from . import views


urlpatterns = [

    path('blog', views.bloghome, name='bloghome'),
    path('blog/<int:blog_id>/', views.blogdetail, name='blogdetail'),
    path('userblog', views.userblog, name='userblog'),
    path('blogadd', views.blogadd, name='blogadd'),
    path('viewauthorprofile', views.viewauthorprofile, name='viewauthorprofile'),

]

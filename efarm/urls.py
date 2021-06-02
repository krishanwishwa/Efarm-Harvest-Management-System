from django.contrib import admin
from django.urls import path,include
from pages import views
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
#connecting all app urls
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('finance/', include('finance.urls')),
    path('pages/', include('pages.urls')),
    path('resources/', include('resources.urls')),
    path('weather/', include('weather.urls')),
    path('fields/', include('fields.urls')),
    path('blogs/', include('blogs.urls')),
    path('prediction/', include('prediction.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

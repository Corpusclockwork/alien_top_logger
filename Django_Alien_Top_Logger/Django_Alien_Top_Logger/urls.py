"""
URL configuration for Django_Alien_Top_Logger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic import RedirectView

def index_view(request):
    return render(request, 'dist/index.html')

def image_view(request):
    return render(request, 'dist/alien_bloc_shape_final.jpg')

def favicon_view(request):
    return render(request, 'dist/alien_top_logger.png')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.authtoken")),
    path("api/v1/", include("climbing_app.urls")),
    path('', index_view, name='index'),  
    path('alien_bloc_shape_final.jpg', image_view, name='image'),  
    path('static/alien_top_logger.png', favicon_view, name='favicon'),  
    path('favicon.ico', RedirectView.as_view(url='/static/alien_top_logger.png')),
]

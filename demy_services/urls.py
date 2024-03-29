"""
URL configuration for demy_services project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    #path("users/", include("django.contrib.auth.urls")),
    #path("", TemplateView.as_view(template_name="homebase.html"), name="home"),
    # If auth is implemented
    #path('login/, include('auth.urls'))
    # place holder for calendar
    path('dashboard/', include('dashboard.urls')),
    path('', include('es_calendar.urls')),
    path('eservices/', include('eservices.urls')),
    path('visa_processing/', include('visa_processing.urls')),
    path('passport_process/', include('passport_process.urls')),
]
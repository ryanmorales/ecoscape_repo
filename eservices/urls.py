from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.eservices, name='eservices'),
    path('service/<int:pk>', views.eservices_service, name='eservices-service'),
]
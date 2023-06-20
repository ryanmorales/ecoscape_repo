from django.urls import path
from . import views

urlpatterns = [

    path('', views.eservices, name='eservices'),
    path('service/<int:pk>', views.eservices_service, name='eservices-service'),

]
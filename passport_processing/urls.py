from django.urls import path
from . import views

urlpatterns = [

    path('new/', views.new_passport, name='new_passport'),
    path('renew/', views.renew_passport, name='renew_passport'),

]
from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_visa_processing, name='add_visa_processing'),

]
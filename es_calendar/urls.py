from django.urls import path
from . import views

urlpatterns = [

    path('calendar/', views.EsCalendar, name='es_calendar'),
    path('all_events/', views.all_events, name='all_events'), 
    path('update/', views.update, name='update'),

]
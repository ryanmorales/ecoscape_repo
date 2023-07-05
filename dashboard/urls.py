from django.urls import path
from .views import (
    Dashboard,
)


urlpatterns = [
    path('dashboard/', Dashboard.dashboard, name='dashboard'),
    path('dashboard/', Dashboard.home, name='home'),
]
from django.urls import path
from . import views
from .views import SanctionDashboard



urlpatterns = [
    path('login/', views.login, name='sanction-login'),
    path('logout/', views.logout,  name="sanction-logout"),
    path('properties_rental/list/', SanctionDashboard.sanction_board, name="properties-rental-list"),
    path('educational_tour/list/', SanctionDashboard.sanction_board, name="educational-tour-list"),
    path('hotel_bookings/list/', SanctionDashboard.sanction_board, name="hotel-bookings-list"),

    path('', SanctionDashboard.sanction_board, name='sanction-board'),

]
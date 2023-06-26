from django.urls import path
from visa_processing import views as visa_views
from passport_process import views as port_views


urlpatterns = [

    path('visa_processing/list/', visa_views.VisaListView.as_view(), name='visa-processing-list'),
    path('passport_process/list/', port_views.PassportListView.as_view(), name='passport-process-list'),

]
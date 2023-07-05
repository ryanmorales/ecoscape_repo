from django.urls import path
from visa_processing.views import VisaListView as ViewVisa
from passport_process.views import PassportListView as ViewPassport


urlpatterns = [
    path('visa_processing/list/', ViewVisa.as_view(), name='visa-processing-list'),
    path('passport_process/list/',ViewPassport.as_view(), name='passport-process-list'),

]
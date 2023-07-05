from django.urls import path
from . import views

urlpatterns = [

    path('visa_processing/', views.VisaListView.as_view(), name='visa-processing'),
    path('visa_processing/list/<int:pk>', views.VisaListView.as_view(), name='visa-processing-list'),
    path('visa_processing/create/', views.VisaCreateView.as_view(), name='visa-processing-create'),
    path('visa_processing/update/<int:pk>', views.VisaUpdateView.as_view(), name='visa-processing-update'),
    path('visa_processing/view/<int:pk>', views.VisaReadView.as_view(), name='visa-processing-view'),
    path('visa_processing/filter/', views.VisaFilterView.as_view(), name='visa-processing-filter'),

]
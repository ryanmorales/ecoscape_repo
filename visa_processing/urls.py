from django.urls import path
from . import views

urlpatterns = [

    path('visa_list', views.VisaListView.as_view(), name='visa-processing-list'),
    path('visa_create/', views.VisaCreateView.as_view(), name='visa-processing-create'),
    path('visa_update/<int:pk>', views.VisaUpdateView.as_view(), name='visa-processing-update'),
    path('visa_view/<int:pk>', views.VisaReadView.as_view(), name='visa-processing-view'),
    path('visa_filter/', views.VisaFilterView.as_view(), name='visa-processing-filter'),

]
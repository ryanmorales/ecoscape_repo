from django.urls import path
from . import views

urlpatterns = [

    path('visa_processing/', views.VisaListView.as_view(), name='visa-processing'),
    path('list/', views.VisaListView.as_view(), name='visa-processing-list'),
    path('create/', views.VisaCreateView.as_view(), name='visa-processing-create'),
    path('update/<int:pk>', views.VisaUpdateView.as_view(), name='visa-processing-update'),
    path('view/<int:pk>', views.VisaReadView.as_view(), name='visa-processing-view'),
    path('filter/', views.VisaFilterView.as_view(), name='visa-processing-filter'),

]
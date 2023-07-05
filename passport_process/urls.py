from django.urls import path
from . import views

urlpatterns = [

    path('passport_process/', views.PassportListView.as_view(), name='passport-process'),
    path('passport_process/list/<int:pk>', views.PassportListView.as_view(), name='passport-process-list'),
    path('passport_process/details/<int:pk>', views.PassportDetailsView.as_view(), name='passport-process-details'),
    path('passport_process/create/', views.PassportCreateView.as_view(), name='passport-process-create'),
    path('passport_process/update/<int:pk>', views.PassportUpdateView.as_view(), name='passport-process-update'),
    path('passport_process/view/<int:pk>', views.PassportReadView.as_view(), name='passport-process-view'),
    path('passport_process/filter/', views.PassportFilterView.as_view(), name='passport-process-filter'),

]
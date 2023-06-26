from django.urls import path
from . import views

urlpatterns = [

    path('passport_process/', views.PassportListView.as_view(), name='passport-process'),
    path('list/', views.PassportListView.as_view(), name='passport-process-list'),
    path('details/<pk>', views.PassportDetailsView.as_view(), name='passport-process-details'),
    path('create/', views.PassportCreateView.as_view(), name='passport-process-create'),
    path('update/<int:pk>', views.PassportUpdateView.as_view(), name='passport-process-update'),
    path('view/<int:pk>', views.PassportReadView.as_view(), name='passport-process-view'),
    path('filter/', views.PassportFilterView.as_view(), name='passport-process-filter'),

]
from django.urls import path
from . import views
from .views import PassportList, PassportDetail

urlpatterns = [

    path('passport_list/', PassportList.as_view(), name='passport-list'),
    path('passport_detail/<pk>', PassportDetail.as_view(), name='passport-detail'),

]
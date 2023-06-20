from django.urls import path
from . import views
from .views import PassportList, PassportDetail

urlpatterns = [

    path('passport_list/', PassportList.as_view(), name='PassportList'),
    path('passport_detail/<pk>', PassportDetail.as_view(), name='PassportDetail'),

]
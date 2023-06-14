from django.urls import path
from . import views
from .views import PassportProcessing as passport

urlpatterns = [

    path('new/', passport.new_passport, name='new_passport'),
    path('renew/', passport.renew_passport, name='renew_passport'),

]
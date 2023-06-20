from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, JsonResponse, HttpResponse
from demy_services.base import BaseViewSet
from rest_framework.decorators import action

from .models import Passport, Appointment, Applicant
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class PassportList(ListView):
    model = Passport
    queryset = Passport.objects.all()


class PassportDetail(DetailView):
    model = Passport


class PassportProcessing(BaseViewSet):

    @staticmethod
    def new_passport(self, request):
        render(BaseViewSet.unauthorized_response())

    @staticmethod
    def renew_passport(self, request):
        pass


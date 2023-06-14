from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, JsonResponse, HttpResponse
from demy_services.base import BaseViewSet
from rest_framework.decorators import action



class PassportProcessing(BaseViewSet):

    @staticmethod
    def new_passport(self, request):
        render(BaseViewSet.unauthorized_response())

    @staticmethod
    def renew_passport(self, request):
        pass


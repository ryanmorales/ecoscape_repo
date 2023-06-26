from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from eservices import models as service_model


class SanctionDashboard(View):
    def sanction_board(request):
        services = service_model.Eservices.objects.filter(services_status=True)
        context = { 'nav_services': services}
        return render(request, 'in_development.html', context)

    def login(self, request):
        pass

    def logout(self, request):
        pass


def login():
    return False

def logout():
    return True

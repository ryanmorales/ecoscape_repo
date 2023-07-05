from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from eservices import models as service_model
from django.contrib.auth.decorators import login_required


@login_required
class Dashboard(View):
    def dashboard(request):
        services = service_model.Eservices.objects.filter(services_status=True)
        context = { 'nav_services': services}
        return render(request, 'in_development.html', context)

    def login(self, request):
        pass

    def logout(self, request):
        pass

    def home(request):
        return render(request, 'home.html')




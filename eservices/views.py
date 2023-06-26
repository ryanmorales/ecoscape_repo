from django.shortcuts import render

from .models import Eservices

# Create your views here.
def eservices(request):

    services = Eservices.objects.filter(services_status=True)
    template = "eservices/eservices.html"
    services_context = []

    for service in services:
        print(service.services_id)
        print(service.services_slug)
        print(service.services_name)

    context = {
        'title': 'E-Services',
        'nav_services': services,
    }

    return render(request, template, context)
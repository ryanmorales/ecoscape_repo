from django.shortcuts import render
from .models import Eservices
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def eservices(request):

    services = Eservices.objects.filter(services_status=True)
    template = "eservices/eservices.html"

    context = {
        'title': 'E-Services',
        'nav_services': services,
    }

    return render(request, template, context)
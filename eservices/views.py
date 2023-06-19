from django.shortcuts import render

from demy_services.settings import BASE_DIR
from demy_services.settings import TEMPLATES

from . models import Eservices
import os

# Create your views here.


def eservices(request):

    services = Eservices.objects.filter(services_status=True)
    context = {'services': services}
    url = TEMPLATES[0]['DIRS'][0] + "/base.html"
    return render(request, url,  context=context)
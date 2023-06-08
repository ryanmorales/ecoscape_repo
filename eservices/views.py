from django.shortcuts import render
from . models import Eservices

# Create your views here.

def eservices(request):
    
    services = Eservices.objects.filter(services_status=True)    
    context = {'services': services}
    return render(request, 'eservices/eservices.html', context=context)
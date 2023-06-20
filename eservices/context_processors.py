from . models import Eservices

def eservices_context(request):
    
    services = Eservices.objects.filter(services_status=True)    
    context = {'services': services}
    return context
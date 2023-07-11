from django.shortcuts import render
from visa_processing.models import Visa
from django.http import JsonResponse
from django.views import View
from eservices.models import Eservices
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def EsCalendar(request):                

    all_events = Visa.objects.filter(appointment_date__isnull=False)    
    services = Eservices.objects.filter(services_status=True)
      
    #out = []                                                                                                             
    #for event in all_events:                                                                                             
     #   out.append({                                                                                                     
      #      'title': event.client_surname,                                                                                         
       #     'or_number': event.or_number,                                                                                              
        #    'start': event.appointment_date,                                                         
         #   'end': event.appointment_date,
        #})
    context = {
        'events':all_events,
        'nav_services': services,
    }
    #return JsonResponse(out, safe=False) 
    return render(request,'es_calendar/es-calendar.html',context)


@login_required
def all_events(request):                                                                                                 
    all_events = Visa.objects.filter(appointment_date__isnull=False)                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({        
            'visa_processing_id': event.visa_processing_id,                                                                                             
            'client': event.client_surname,                                                                                         
            'or_number': event.or_number,                                                                                              
            'start': event.appointment_date.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.appointment_date.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
        print(event.appointment_date.strftime("%m/%d/%Y, %H:%M:%S"))

    return JsonResponse(out, safe=False)


@login_required
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("client", None)
    or_number = request.GET.get("or_number", None)
    id = request.GET.get("visa_processing_id", None)
    event = Visa.objects.filter(appointment_date__isnull=False, visa_processing_id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
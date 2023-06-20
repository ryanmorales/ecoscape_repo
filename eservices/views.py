from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from demy_services.settings import BASE_DIR
from demy_services.settings import TEMPLATES

from . models import Eservices
from passport_process import models as port_models
from visa_processing import models as visa_models
import os

# Create your views here.


def eservices(request,):

    services = Eservices.objects.filter(services_status=True)
    context = {
        'services': services,
        'title': 'E-Services',
    }
    url = TEMPLATES[0]['DIRS'][0] + "/base.html"
    return render(request, url,  context=context)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def eservices_service(request, pk):
    services = Eservices.objects.filter(services_status=True)

    context = {
        'services': services,
    }

    if pk == 2:
        url = 'visa_processing/visa-processing-list.html'

        context['visa_processing_list'] = visa_models.Visa.objects.all()

        return render(request, url, context=context)
    elif pk == 3:
        for service in services:
            print(service)

        context['object_list'] = port_models.Passport.objects.all()
        context['apply_type'] = port_models.Passport.APPLICATION_TYPE
        print(context['apply_type'])

        url = 'passport_process/passport-process-list.html'

        return render(request, url , context=context)
    else:
        context = {
            'services': services,
            "success": False,
            "error_message": "Site coming soon.",
        }

        context["extra_info"] = "In Development"

        return Response(context, status=HTTP_200_OK, template_name="in_development.html")
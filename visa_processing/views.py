from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Visa
from visa_processing.forms import VisaProcessingForm, VisaFilterForm
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalFormView
from eservices import models as e_models


# Create your views here.
class VisaListView(generic.ListView):
   
    context_object_name = 'visa_processing_list'
    template_name = 'visa_processing/visa-processing-list.html'
    paginate_by = 5

    def get_queryset(self):

        print(self.request.GET.get('or_number'))
        if self.request.GET.get('client_surname'):
            return Visa.objects.filter(client_surname__contains=self.request.GET.get('client_surname'))
        elif self.request.GET.get('or_number'):
            return Visa.objects.filter(or_number__contains=self.request.GET.get('or_number'))
        else:
            return Visa.objects.order_by('-date_updated')

        #return super().get_queryset()


class VisaCreateView(BSModalCreateView):
    template_name = 'visa_processing/visa-processing-create.html'
    form_class = VisaProcessingForm
    success_message = 'Success: Visa Processing transaction was created.'
    success_url = reverse_lazy('visa-processing-list')


class VisaUpdateView(BSModalUpdateView):
    services = e_models.objects.filter(services_status=True)
    context = {
        'services': services,
    }
    model = Visa
    context_object_name = 'visa-processing-update'
    template_name = 'visa_processing/visa-processing-update.html'
    form_class = VisaProcessingForm
    context_object_name = 'visa_processing_view'
    success_message = 'Success: Visa Processing transaction was updated.'
    success_url = reverse_lazy('visa-processing-list', context)


class VisaReadView(BSModalReadView):
    model = Visa
    context_object_name = 'visa-processing-view'
    template_name = 'visa_processing/visa-processing-view.html'


class VisaFilterView(BSModalFormView):
    template_name = 'visa_processing/visa-processing-filter.html'
    form_class = VisaFilterForm

    def form_valid(self, form):
        self.filter = '?client_surname=' + form.cleaned_data['client_surname'] + '&or_number=' + form.cleaned_data['or_number']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('visa-processing-list') + self.filter
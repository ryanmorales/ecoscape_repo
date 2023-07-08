from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Visa
from . apps import VisaProcessingConfig as visa_config
from visa_processing.forms import VisaProcessingForm, VisaFilterForm
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalFormView
from eservices.models import Eservices


# Create your views here.
class VisaListView(generic.ListView):
    context_object_name = 'visa_processing_list'
    template_name = 'visa_processing/visa-processing-list.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('client_surname'):
            return Visa.objects.filter(client_surname__contains=self.request.GET.get('client_surname'))
        elif self.request.GET.get('or_number'):
            return Visa.objects.filter(or_number__contains=self.request.GET.get('or_number'))
        else:
            return Visa.objects.order_by('-date_updated')

        #return super().get_queryset()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Visa Processing List'
        context['app_name'] = visa_config.__name__

        return context


class VisaCreateView(BSModalCreateView):
    template_name = 'visa_processing/visa-processing-create.html'
    form_class = VisaProcessingForm
    success_message = 'Success: Visa Processing transaction was created.'
    success_url = reverse_lazy('visa-processing-list')


class VisaUpdateView(BSModalUpdateView):
    model = Visa
    context_object_name = 'visa-processing-update'
    template_name = 'visa_processing/visa-processing-update.html'

    form_class = VisaProcessingForm
    context_object_name = 'visa_processing_view'
    success_message = 'Success: Visa Processing transaction was updated.'
    success_url = reverse_lazy('visa-processing-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Visa Processing List'
        context['app_name'] = visa_config.name

        return context

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
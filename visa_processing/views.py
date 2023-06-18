from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Visa
from visa_processing.forms import VisaProcessingForm
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView


# Create your views here.
class VisaListView(generic.ListView):
    model = Visa
    context_object_name = 'visa_processing_list'
    template_name = 'visa_processing/visa-processing-list.html'


class VisaCreateView(BSModalCreateView):
    template_name = 'visa_processing/visa-processing-create.html'
    form_class = VisaProcessingForm
    success_message = 'Success: Visa Processing transaction was created.'
    success_url = reverse_lazy('visa-processing-list')

class VisaUpdateView(BSModalUpdateView):
    model = Visa
    template_name = 'visa_processing/visa-processing-update.html'
    form_class = VisaProcessingForm
    success_message = 'Success: Visa Processing transaction was updated.'
    success_url = reverse_lazy('visa-processing-list')

class VisaReadView(BSModalReadView):
    model = Visa
    context_object_name = 'visa_processing_view'
    template_name = 'visa_processing/visa-processing-view.html'

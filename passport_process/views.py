from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Passport
from .apps import PassportProcessConfig as pass_config
from passport_process.forms import PassportProcessForm, PassportFilterForm
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalFormView
from eservices.models import Eservices


# Create your views here.
class PassportListView(generic.ListView):
    content_name_object = 'passport_process_list'
    template_name = 'passport_process/passport-process-list.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('client_surname'):
            return Passport.objects.filter(client_surname__contains=self.request.GET.get('client_surname'))
        elif self.request.GET.get('or_number'):
            return Passport.objects.filter(or_number__contains=self.request.GET.get('or_number'))
        else:
            return Passport.objects.order_by('-date_updated')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Passport Processing List'
        context['app_name'] = pass_config.name

        return context


class PassportDetailsView(generic.DetailView):
    content_name_object = 'passport_process_details'
    template_name = 'passport_process/passport-process-details.html'

    passport = Passport
    model = Passport


class PassportCreateView(BSModalCreateView):
    model = Passport
    context_object_name = 'passport_process_create'
    template_name = 'passport_process/passport-process-create.html'

    form_class = PassportProcessForm
    success_message = 'Success: New Passport Processing transaction was created.'
    success_url = reverse_lazy('passport-process-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Passport Processing List'

        return context

class PassportUpdateView(BSModalUpdateView):
    model = Passport
    context_object_name = 'passport_process_update'
    template_name = 'passport_process/passport-process-update.html'

    form_class = PassportProcessForm
    context_object_name = 'passport_process_view'
    success_message = 'Success: Passport Process transaction was updated.'
    success_url = reverse_lazy('passport-process-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Passport Processing List'

        return context


class PassportReadView(BSModalReadView):
    model = Passport
    context_object_name = 'passport_process_view'
    template_name = 'passport_process/passport-process-view.html'


class PassportFilterView(BSModalFormView):
    form_class = PassportFilterForm
    template_name = 'passport_process/passport-process-filter.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Passport Processing List'
        context['app_name'] = pass_config.name

        return context

    def form_valid(self, form):
        self.filter = '?client_surname=' + form.cleaned_data['client_surname'] + '&or_number=' + form.cleaned_data['or_number']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('passport-process-list') + self.filter
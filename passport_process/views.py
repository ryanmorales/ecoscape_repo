from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Passport
from passport_process.forms import PassportProcessForm, PassportFilterForm
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalFormView
from eservices.models import Eservices


class PassportListView(generic.ListView):
    content_name_object = 'passport_process_list'
    template_name = 'passport_process/passport-process-list.html'
    path_name = 'passport-process-list'
    paginate_by = 5

    def get_queryset(self):
        surname = self.request.GET.get('client_surname') or None
        o_r_num = self.request.GET.get('or_number') or None

        if surname:
            return Passport.objects.filter(client_surname__contains=surname)
        elif o_r_num:
            return Passport.objects.filter(or_number__contains=o_r_num)
        else:
            return Passport.objects.order_by('-date_updated')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Passport Processing List'

        return context


class PassportDetailsView(generic.DetailView):
    content_name_object = 'passport_process_details'
    template_name = 'passport_process/passport-process-details.html'

    passport = Passport
    model = Passport


class PassportCreateView(generic.CreateView):
    model = Passport
    template_name = 'passport_process/passport-process-create.html'
    form_class = PassportProcessForm
    success_message = 'Success: New Passport Processing transaction was created.'
    success_url = reverse_lazy('passport-process-list')


class PassportUpdateView(generic.UpdateView):
    model = Passport
    context_object_name = 'passport_process_update'
    template_name = 'passport_process/passport-process-update.html'

    form_class = PassportProcessForm
    context_object_name = 'passport_process_view'
    success_message = 'Success: Visa Processing transaction was updated.'
    success_url = reverse_lazy('visa-processing-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        services = Eservices.objects.filter(services_status=True)
        context["nav_services"] = services
        context['title'] = 'Visa Processing List'

        return context


class PassportReadView(BSModalReadView):
    model = Passport


class PassportFilterView(BSModalFormView):
    form_class = PassportFilterForm
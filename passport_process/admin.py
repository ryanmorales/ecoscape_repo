from django.contrib import admin
from django import forms
from . models import Passport


class PassportProcessAdminForm(forms.ModelForm):
    class Meta:
        model = Passport
        exclude = ['created_by', 'updated_by', 'date_created', 'date_updated']
        widgets = {'appointment_date': forms.DateInput(attrs={'type': 'date'})}


class PassportProcessAdmin(admin.ModelAdmin):
    list_display =[
        'passport_process_id',
        'client_surname',
        'client_given_name',
        'client_contact_number',
        'application_type',
        'status',
        'created_by',
        'updated_by',
        'date_created',
        'date_updated',
    ]
    form = PassportProcessAdminForm

    def save_model(self, request, obj, form, change):

        if not obj.passport_process_id:
            obj.created_by = request.user
            obj.updated_by = request.user

        if change and obj.passport_process_id:
            obj.updated_by = request.user

        return super().save_model(request, obj, form, change)

    def name(self, obj):
        return "%s %s" % (obj.client_given_name, obj.client_surname)

    name.short_description = "Passport Process"


admin.site.register(Passport, PassportProcessAdmin)
admin.site.site_header = "EcoScape Travel and Tours Admin"
admin.site.site_title = "Passport Processing Admin"
admin.site.index_title = "Passport Processing Admin"
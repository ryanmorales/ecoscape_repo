from django.contrib import admin
from django import forms
from django.forms import Media
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from . models import Visa


# Register your models here.

class Visa_Processing_Admin_Form(forms.ModelForm):
    
    class Meta:
        model = Visa
        fields = '__all__'
    

class Visa_Processing_Admin(admin.ModelAdmin):
    list_display =[
        'visa_processing_id', 
        'applicant_surname', 
        'applicant_given_name', 
        'applicant_passport_number', 
        'visa_service_type', 
        'visa_status', 
        'visa_type',
    ]
    form = Visa_Processing_Admin_Form

    def get_form(self, request, obj=None, **kwargs):
        
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['visa_type'].widget.attrs['data-dependency'] = 'non_immigrant_visa_type'
        form.base_fields['non_immigrant_visa_type'].widget.attrs['data-target'] = 'visa_type'

        return form

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'js/visa_processing_admin.js',
        )


    def get_fieldsets(self, request, obj=None):

        fieldsets = super().get_fieldsets(request, obj)
        fieldsets.append(('Custom JavaScript', {
            'description': mark_safe(
                'Make sure to include the <a href="{0}" target="_blank">visa_processing_admin.js</a> JavaScript file in your static files directory.'.format(
                    reverse_lazy('admin:visa_processing_visa_changelist'))),
            'classes': ('collapse',),
            'fields': (),
        }))
        return fieldsets

admin.site.register(Visa, Visa_Processing_Admin)
admin.site.site_header = "EcoScape Travel and Tours Admin"
admin.site.site_title = "Visa Processing Admin"
admin.site.index_title = "Visa Processing Admin"
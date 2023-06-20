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
        exclude = ['created_by','updated_by','date_created','date_updated']    

class Visa_Processing_Admin(admin.ModelAdmin):
    list_display =[
        'visa_processing_id', 
        'client_surname', 
        'client_given_name', 
        'visa_service_type', 
        'status', 
        'created_by',
        'updated_by',
        'date_created',
        'date_updated',
    ]
    form = Visa_Processing_Admin_Form
    
    def save_model(self, request, obj, form, change):
        
        if not obj.visa_processing_id:
            obj.created_by = request.user
            obj.updated_by = request.user
        
        if change and obj.visa_processing_id:
            obj.updated_by = request.user

        return super().save_model(request, obj, form, change)

admin.site.register(Visa, Visa_Processing_Admin)
admin.site.site_header = "EcoScape Travel and Tours Admin"
admin.site.site_title = "Visa Processing Admin"
admin.site.index_title = "Visa Processing Admin"
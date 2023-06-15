from django.contrib import admin
from . models import Eservices

# Register your models here.

@admin.register(Eservices)
class EservicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'services_slug': ('services_name',)}
    list_display =[
        'services_id', 'services_name', 'services_date_created', 'services_created_by', 'services_date_updated', 'services_updated_by', 'services_status'
    ]
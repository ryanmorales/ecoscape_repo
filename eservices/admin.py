from django.contrib import admin
from . models import Eservices

# Register your models here.

@admin.register(Eservices)
class EservicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'services_slug': ('services_name',)}
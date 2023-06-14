from django.contrib import admin
from . models import Passport, Applicant, Appointment




class PassportAdmin(admin.ModelAdmin):
    list_display =[
        'id', 'applicant', 'basis_of_citizenship', 'application_type', 'foreign_passport_holder'
    ]

    search_fields = [
        'id'
    ]


admin.site.register(Passport, PassportAdmin)


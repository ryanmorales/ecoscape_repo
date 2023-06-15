from django.contrib import admin
from . models import Passport, Applicant, Appointment


class PassportAdmin(admin.ModelAdmin):
    list_display =[
        'id', 'applicant', 'basis_of_citizenship', 'application_type', 'foreign_passport_holder'
    ]

    search_fields = [
        'id'
    ]

class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email_add'
    ]

    search_fields = [
        'first_name', 'last_name', 'email_add'
    ]

class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'appointment_type', 'region', 'country', 'site'
    ]

    search_fields = [
        'appointment_type'
    ]


admin.site.register(Passport, PassportAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Appointment, AppointmentAdmin)


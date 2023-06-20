from django.contrib import admin
from . models import PassportProcess, PassportApplicant, PassportAppointment


class PassportProcessAdmin(admin.ModelAdmin):
    list_display =[
        'id', 'client_surname', 'client_given_name', 'client_contact_number', 'passport_application_type', 'passport_applicant_count'
    ]

    search_fields = [
        'client_surname', 'client_given_name'
    ]

    def name(self, obj):
        return "%s %s" % (obj.client_given_name, obj.client_surname)

    list_filter = (
        ('passport_applicant', admin.RelatedFieldListFilter),
        ('passport_application_type'),
        ('passport_applicant_count'),
    )

    name.short_description = "Passport Process"


class PassportApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email_address'
    ]

    search_fields = [
        'first_name', 'last_name', 'email_address'
    ]


class PassportAppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'appointment_type', 'location_site', 'date', 'time'
    ]

    search_fields = [
        'appointment_type', 'date', 'time'
    ]




admin.site.register(PassportProcess, PassportProcessAdmin)
admin.site.register(PassportApplicant, PassportApplicantAdmin)
admin.site.register(PassportAppointment, PassportAppointmentAdmin)


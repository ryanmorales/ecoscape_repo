from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL, DO_NOTHING
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Passport(models.Model):
    """
    Passport model definition
    """
    APPLICATION_TYPE = [
        ('NEW', 'New Application'),
        ('RENEW', 'Passport Renewal'),
        ('LOST', 'Lost Passport')
    ]

    CITIZEN_BASIS = [
        ('BIRTH', 'PSA Birth Certificate'),
        ('VOTER', 'Identification Certificate of Election'),
        ('MARRIED', 'PSA Marriage Certificate'),
        ('NATURAL', 'Identification Certificate of Naturalization'),
        ('RA9225', 'Dual Citizenship Document'),
        ('OTHER', 'Others')
    ]

    STATUS_CHOICES = (
        ('In-Progress', 'IN PROGRESS'),
        ('Deferred', 'DEFERRED'),
        ('Completed', 'COMPLETED'),
    )

    passport_process_id = models.AutoField(primary_key=True)
    client_surname = models.CharField(max_length=100, db_index=True, blank=False, default=None)
    client_given_name = models.CharField(max_length=100, db_index=True, blank=False, default=None)
    client_contact_number = PhoneNumberField(blank=True)
    applicant_surname = models.CharField(max_length=100, db_index=True, blank=False, default=None)
    applicant_given_name = models.CharField(max_length=100, db_index=True, blank=False, default=None)
    citizen_cert = models.CharField(max_length=25, choices=CITIZEN_BASIS, blank=True)
    foreign_passport = models.BooleanField(default=False)
    application_type = models.CharField(max_length=25, choices=APPLICATION_TYPE, blank=False)
    appointment_date = models.DateField(null=True, blank=True)
    appointment_location = models.CharField(max_length=250, null=True, blank=True)
    epp_passport_name = models.CharField(max_length=250, null=True, blank=True)
    epp_passport_number = models.CharField(max_length=60, null=True, blank=True)
    epp_passport_date_issued = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=None)
    or_number = models.CharField(max_length=50, blank=False)
    or_receipt = models.ImageField(upload_to='system/management/images/receipts/', default=None, blank=True)
    service_fee = models.DecimalField(max_digits=9, decimal_places=2, default=None)
    passport_fee = models.DecimalField(max_digits=9, decimal_places=2, default=None)
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="created_passport_process",on_delete=models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name="updated_passport_process",on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Passport Process'
        verbose_name_plural = 'Passport Application/Renewal Process'

    def __str__(self):
        """ Return string passport applicant """
        return self.epp_passport_name or self.get_full_name()

    def get_full_name(self):
        return "%s %s" % (self.client_given_name, self.client_surname)



"""
class PassportApplicant(models.Model):
    Passport Applicant model definition
    
    passport_process = models.ForeignKey(PassportProcess, related_name="passport_process", on_delete=CASCADE, db_index=True )
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=False, blank=False)
    # Contact Information
    present_address = models.CharField(max_length=254, null=False, blank=False)
    contact_person = models.CharField(max_length=100, null=False, blank=False)
    contact_number = models.CharField(max_length=60, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="created_passport_applicant", on_delete=models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name="updated_passport_applicant", on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Passport Applicant'
        verbose_name_plural = 'Passport Applicant Details'

    def __str__(self):
        return self.full_name or self.get_full_name()

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
        
        
class PassportAppointment(models.Model):
    Appointment model definition
    
    INDIVIDUAL = 1
    GROUP = 2

    APPOINTMENT_TYPE = [
        (INDIVIDUAL, 'Individual Appointment'),
        (GROUP, 'Group Appointment')
    ]

    appointment_type = models.IntegerField(choices=APPOINTMENT_TYPE, default=INDIVIDUAL)
    location_site = models.CharField(max_length=250, db_index=True, blank=False, default=None)
    contact_number = PhoneNumberField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="created_passport_appointment", on_delete=models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name="updated_passport_appointment", on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Passport Appointment'
        verbose_name_plural = 'Passport Application Appointment Schedule'

    def __str__(self):
        for k, v in self.APPOINTMENT_TYPE:
            return v if k == self.appointment_type else None


"""
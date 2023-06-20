from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Visa(models.Model):

    SERVICE_TYPE_CHOICES = (
        ('New Application','NEW APPLICATION'),
        ('Renewal','RENEWAL'),
    )
    STATUS_CHOICES = (
        ('In-Progress','IN PROGRESS'),
        ('Deferred','DEFERRED'),
        ('Completed','COMPLETED'),
    )    
    COUNTRY_CHOICES = (
        ('none','Please Choose.'),
        ('usa','US'),
        ('canada','CANADA'),
        ('australia','AUSTRALIA'),
        ('japan','JAPAN'),
        ('korea','KOREA'),
        ('germany','GERMANY'),
        ('united_kingdom','UNITED KINGDOM'),
    )

    visa_processing_id = models.AutoField(primary_key=True)
    client_surname = models.CharField(max_length=250, db_index=True, blank=False, default=None)
    client_given_name = models.CharField(max_length=250, blank=False, default=None)
    client_contact_number = PhoneNumberField(blank=True)
    applicant_surname = models.CharField(max_length=250, blank=False)
    applicant_given_name = models.CharField(max_length=250, blank=False)
    visa_service_type = models.CharField(max_length=25, choices=SERVICE_TYPE_CHOICES, blank=False)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=None)
    country_visa = models.CharField(max_length=25, choices=COUNTRY_CHOICES, default=None)
    visa_form = models.BooleanField(default=False)
    appointment_date = models.DateTimeField(null=True, blank=True)
    or_number = models.CharField(max_length=50, blank=False)
    or_receipt = models.ImageField(upload_to='images/', default=None, blank=True)
    service_fee = models.DecimalField(max_digits=9,decimal_places=2, default=None)
    visa_fee = models.DecimalField(max_digits=9,decimal_places=2, default=None)
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create_visa_transaction')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update_visa_transaction')

    class Meta:
        verbose_name = 'Visa Processing'
        verbose_name_plural = 'Visa Processing'


    def __str__(self):
        return self.client_given_name

    
from django.db import models

# Create your models here.
class Non_Immigrant_Visa_choices(models.TextChoices):
    none = "N/A"
    business_tourist_visa = "Business-Tourist Visa"
    work_visa = "Work Visa"
    student_visa = "Student Visa"
    exchange_visitor_visa = "Exchange Visitor Visa"
    transit_ship_crew_visa = "Transit-Ship Crew Visa"
    religious_worker_visa = "Religious Worker Visa"
    domestic_employee_visa = "Domestic Employee Visa"
    journalist_media_visa = "Journalist-Media Visa"
    treaty_investors_traders_visa = "Treaty Investors-Traders Visa"
    cnmi_saipan_visa = "CNMI Saipan Visa"
    niv_types_visa = "NIV Type Visa"


class Visa(models.Model):

    SEX_CHOICES = (
        ('male','MALE'),
        ('female','FEMALE'),
    )

    visa_processing_id = models.AutoField(primary_key=True)
    applicant_surname = models.CharField(max_length=250, db_index=True)
    applicant_given_name = models.CharField(max_length=250)
    applicant_passport_number = models.CharField(max_length=250)
    applicant_sex = models.CharField(max_length=10, choices=SEX_CHOICES, default=None)
    applicant_birthdate = models.DateField(max_length=10)
    applicant_age = models.IntegerField()

    SERVICE_TYPE_CHOICES = (
        ('New Application','NEW APPLICATION'),
        ('Renewal','RENEWAL'),
    )
    visa_service_type = models.CharField(max_length=25, choices=SERVICE_TYPE_CHOICES, default=None)

    STATUS_CHOICES = (
        ('Deferred','DEFERRED'),
        ('In-Progress','IN PROGRESS'),
        ('Completed','COMPLETED'),
    )
    visa_status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=None)
    
    TYPE_CHOICES = (
        ('Non Immigrant Visa','NON-IMMIGRANT VISA'),
        ('Immigrant','IMMIGRANT VISA'),
    )
    visa_type = models.CharField(max_length=25, choices=TYPE_CHOICES, default=None)

    non_immigrant_visa_type = models.CharField(max_length=100, choices=Non_Immigrant_Visa_choices.choices, default=None)

    class Meta:
        verbose_name = 'Visa Processing'
        verbose_name_plural = 'Visa Processing'


    def __str__(self):
        return self.applicant_surname

    
from django.db import models
from django.db.models import CASCADE, SET_NULL, DO_NOTHING

# Create your models here.
class Passport(models.Model):
    """
    Passport model definition
    """

    NEW = 1
    RENEW = 2
    LOST = 3

    APPLICATION_TYPE = [
        (NEW, 'New Application'),
        (RENEW, 'Passport Renewal'),
        (LOST, 'Lost Passport')
    ]

    BIRTH = 1
    VOTER = 2
    MARRIED = 3
    NATURAL = 4
    RA9225 = 5
    OTHER = 0

    CITIZEN_BASIS = [
        (BIRTH, 'PSA Birth Certificate'),
        (VOTER,'Identification Certificate of Election'),
        (MARRIED, 'PSA Marriage Certificate'),
        (NATURAL, 'Identification Certificate of Naturalization'),
        (RA9225, 'Dual Citizenship Document'),
        (OTHER, 'Others')
    ]

    applicant = models.ForeignKey(Applicant, on_delete=CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=CASCADE)
    passport_name = models.CharField(max_length=100, null=True, blank=True)
    passport_number = models.CharField(max_length=60, null=True, blank=True)
    date_issue = models.CharField(max_length=60, null=True, blank=True)
    issuing_auth = models.CharField(max_length=100, null=True, blank=True)
    application_type = models.IntegerField(choices=APPLICATION_TYPE, default=NEW)
    basis_of_citizenship = models.IntegerField(choices=CITIZEN_BASIS, default=OTHER)
    has_foreign_passport = models.BooleanField(default=False)
    emergency_contact_person = models.CharField(max_length=100, null=False, blank=False)
    emergency_contact_number = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        verbose_name = 'Passport'
        verbose_name_plural = 'Passport Application Processing'

    def __str__(self):
        """ Return string passport applicant """
        return self.passport_name or self.get_full_name()

    def get_full_name(self):
        return "%s %s" % (self.applicant.first_name, self.applicant.last_name)


class Appointment(models.Model):
    """
    Appointment model definition
    """

    INDIVIDUAL = 1
    GROUP = 2

    APPOINTMENT_TYPE = [
        (INDIVIDUAL, 'Individual Appointment'),
        (GROUP, 'Group Appointment')
    ]


    appointment_type = models.IntegerField(choices=APPOINTMENT_TYPE, default=INDIVIDUAL)
    region = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    site = models.CharField(max_length=60)
    office_name = models.CharField(max_length=100)
    office_add = models.CharField(max_length=254)
    contact_number = models.CharField(max_length=60)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Passport Application Appointment'



class Applicant(models.Model):
    """
    Passport Applicant model definition
    """

    LEGIT = 1
    ILLEGIT = 2

    LEGITIMACY = [
        (LEGIT, 'Legitimate'),
        (ILLEGIT, 'Illegitimate')
    ]

    passport = models.ForeignKey(Passport, on_delete=CASCADE)
    mobile_number = models.CharField(max_length=60, null=False, blank=False)
    email_add = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    first_name = models.CharField(max_length=60, null=False, blank=False)
    gender = models.CharField(max_length=60, null=False, blank=False)
    civil_status = models.CharField(max_length=60, null=False, blank=False)
    birth_date = models.CharField(max_length=60, null=False, blank=False)
    birth_legitimacy = models.IntegerField(choices=LEGITIMACY, default=LEGIT)
    birth_country = models.CharField(max_length=60, null=False, blank=False)
    birth_province = models.CharField(max_length=60, null=False, blank=False)
    birth_city = models.CharField(max_length=60, null=False, blank=False)
    father_last_name = models.CharField(max_length=60, null=False, blank=False)
    father_given_name = models.CharField(max_length=60, null=False, blank=False)
    father_citizenship = models.CharField(max_length=60, null=False, blank=False)
    mother_maiden_last_name = models.CharField(max_length=60, null=False, blank=False)
    mother_given_name = models.CharField(max_length=60, null=False, blank=False)
    mother_citizenship = models.CharField(max_length=60, null=False, blank=False)

    #Contact Information
    current_add = models.CharField(max_length=254, null=False, blank=False)
    current_province = models.CharField(max_length=60, null=False, blank=False)
    current_country = models.CharField(max_length=60, null=False, blank=False)
    occupation = models.CharField(max_length=60, null=False, blank=False)
    office_number = models.CharField(max_length=60, null=True)
    office_add = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name = 'Applicant Profile'
        verbose_name_plural = 'Passport Applicant Profile'




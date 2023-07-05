# Generated by Django 4.2.2 on 2023-06-25 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passport_process', '0003_passportapplicant_passportappointment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('passport_process_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_surname', models.CharField(db_index=True, default=None, max_length=100)),
                ('client_given_name', models.CharField(db_index=True, default=None, max_length=100)),
                ('client_contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('applicant_surname', models.CharField(db_index=True, default=None, max_length=100)),
                ('applicant_given_name', models.CharField(db_index=True, default=None, max_length=100)),
                ('citizen_cert', models.CharField(blank=True, choices=[('BIRTH', 'PSA Birth Certificate'), ('VOTER', 'Identification Certificate of Election'), ('MARRIED', 'PSA Marriage Certificate'), ('NATURAL', 'Identification Certificate of Naturalization'), ('RA9225', 'Dual Citizenship Document'), ('OTHER', 'Others')], max_length=25)),
                ('foreign_passport', models.BooleanField(default=False)),
                ('application_type', models.CharField(choices=[('NEW', 'New Application'), ('RENEW', 'Passport Renewal'), ('LOST', 'Lost Passport')], max_length=25)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_location', models.CharField(blank=True, max_length=250, null=True)),
                ('epp_passport_name', models.CharField(blank=True, max_length=250, null=True)),
                ('epp_passport_number', models.CharField(blank=True, max_length=60, null=True)),
                ('epp_passport_date_issued', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('In-Progress', 'IN PROGRESS'), ('Deferred', 'DEFERRED'), ('Completed', 'COMPLETED')], default=None, max_length=25)),
                ('or_number', models.CharField(max_length=50)),
                ('or_receipt', models.ImageField(blank=True, default=None, upload_to='system/management/images/receipts/')),
                ('service_fee', models.DecimalField(decimal_places=2, default=None, max_digits=9)),
                ('passport_fee', models.DecimalField(decimal_places=2, default=None, max_digits=9)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_passport_process', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_passport_process', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Passport Process',
                'verbose_name_plural': 'Passport Application/Renewal Process',
            },
        ),
        migrations.RemoveField(
            model_name='passportappointment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='passportappointment',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='passportprocess',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='passportprocess',
            name='passport_appointment',
        ),
        migrations.RemoveField(
            model_name='passportprocess',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='PassportApplicant',
        ),
        migrations.DeleteModel(
            name='PassportAppointment',
        ),
        migrations.DeleteModel(
            name='PassportProcess',
        ),
    ]
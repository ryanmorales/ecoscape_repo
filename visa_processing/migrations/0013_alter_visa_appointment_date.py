# Generated by Django 4.2.2 on 2023-06-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_processing', '0012_alter_visa_or_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

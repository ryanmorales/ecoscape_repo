# Generated by Django 4.2.2 on 2023-06-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_processing', '0004_visa_visa_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='visa_status',
            field=models.CharField(choices=[('Deferred', 'DEFERRED'), ('In-Progress', 'IN PROGRESS'), ('Completed', 'COMPLETED')], default=None, max_length=25),
        ),
    ]

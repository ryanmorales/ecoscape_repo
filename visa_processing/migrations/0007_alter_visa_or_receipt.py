# Generated by Django 4.2.2 on 2023-06-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_processing', '0006_remove_visa_applicant_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='or_receipt',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
    ]
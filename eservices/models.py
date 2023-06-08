from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Eservices(models.Model):
    
    services_id = models.AutoField(primary_key=True)
    services_name = models.CharField(max_length=250, db_index=True)
    services_description = models.CharField(max_length=250)
    services_date_created = models.DateTimeField(auto_now_add=True)
    services_date_updated = models.DateTimeField(auto_now=True)
    services_created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='create')
    services_updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='update')
    services_status = models.BooleanField(default=False)
    services_slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.services_name

from django.db import models

from services.models import Service

class ServiceUser(models.Model):
    name = models.CharField(blank=True, max_length=100)
    contact_info = models.TextField(blank=True)
    services = models.ManyToManyField(Service)

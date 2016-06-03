from django.db import models

class Provider(models.Model):
    name = models.CharField(blank=True, max_length=400)

class Service(models.Model):
    service_id = models.CharField(primary_key=True, max_length=100)
    service_name = models.CharField(blank=True, max_length=400)
    provider = models.ForeignKey(Provider)
    raw_html = models.TextField(blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ("service_detail", [self.pk,])

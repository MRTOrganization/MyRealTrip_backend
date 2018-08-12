from django.db import models


class AccomInfo(models.Model):
    attraction = models.CharField(max_length=200, blank=True)
    depart_date = models.CharField(max_length=100, blank=True)
    return_date = models.CharField(max_length=100, blank=True)


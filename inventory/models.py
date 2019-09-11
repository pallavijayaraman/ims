from django.conf import settings
from django.db import models
from django.utils import timezone


class Catalogue(models.Model):
    category = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    entry_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.entry_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category
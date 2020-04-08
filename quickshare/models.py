from django.db import models
from django.conf import settings
from django.utils import timezone

class Card(models.Model):
    sender = models.CharField(max_length=32)
    header = models.CharField(max_length=64)
    text = models.TextField()
    attachment = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header

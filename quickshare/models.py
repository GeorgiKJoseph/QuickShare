from django.db import models
from django.conf import settings
from django.utils import timezone

class Card(models.Model):
    sender = models.CharField(max_length=32)
    header = models.CharField(max_length=64)
    text = models.TextField()
    atmnt0 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt1 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt2 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt3 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt4 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt5 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt6 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt7 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt8 = models.FileField(upload_to='files/',blank=True,null=True)
    atmnt9 = models.FileField(upload_to='files/',blank=True,null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header

from django.db import models
from django.utils import timezone

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    importer = models.BooleanField(default = False)
    date_importation = models.DateTimeField(auto_now_add=True)
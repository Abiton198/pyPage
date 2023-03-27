from django.db import models


# Create your models here.
class Hotel(models.Model):
    image_url = models.CharField(max_length=2085)
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

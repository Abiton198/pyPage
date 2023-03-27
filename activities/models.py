from django.db import models


# Create your models here.
class Activity(models.Model):
    small_title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=2085)

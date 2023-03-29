from django.db import models


# Create your models here.
class About(models.Model):
    image_url = models.CharField(max_length=2085)
    description = models.CharField(max_length=500)
    small_title = models.CharField(max_length=50)


from django.db import models


# Create your models here.
class Travel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    image_url = models.CharField(max_length=2085)


from django.db import models

# Create your models here.


class Address(models.Model):
    country = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=40)
    road = models.CharField(max_length=120)

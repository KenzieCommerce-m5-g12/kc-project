from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    isAdm = models.BooleanField()
    email = models.EmailField(max_length=120, unique=True)

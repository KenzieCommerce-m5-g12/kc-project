from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TypeUserChoices(models.TextChoices):
    USER = "user"
    SELLER = "seller"
    ADMIN = "admin"


class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    isAdmin = models.BooleanField(default=False, null=True)
    email = models.EmailField(max_length=120, unique=True)
    typeUser = models.CharField(
        choices=TypeUserChoices.choices, default=TypeUserChoices.USER, null=True
    )

    address = models.OneToOneField(
        "address.Address", on_delete=models.CASCADE, related_name="user"
    )

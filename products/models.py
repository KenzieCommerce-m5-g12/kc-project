from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    category = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    url = models.TextField()
    description = models.TextField()
    stock = models.PositiveIntegerField()
    # user = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.CASCADE,
    #     related_name="products"
    # )

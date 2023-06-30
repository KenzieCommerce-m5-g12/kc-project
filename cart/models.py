from django.db import models


class Cart(models.Model):
    products = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cart"
    )

from django.db import models


class Cart(models.Model):
    products = models.ForeignKey(
        "products.Products", on_delete=models.CASCADE, related_name="cart"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )
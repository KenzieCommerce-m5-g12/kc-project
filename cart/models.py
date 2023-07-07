from django.db import models


class Cart(models.Model):
    class Meta:
        ordering = ["id"]

    products_cart = models.ManyToManyField(
        "products.Product", through="cart.CartProduct", related_name="cart_products"
    )

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )


class CartProduct(models.Model):
    class Meta:
        ordering = ["id"]

    cart = models.ForeignKey(
        "cart.Cart", on_delete=models.CASCADE, related_name="cart_data"
    )

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="product_data"
    )

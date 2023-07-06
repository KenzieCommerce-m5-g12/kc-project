from django.db import models


class Favorite(models.Model):
    class Meta:
        ordering = ["id"]

    products_favorite = models.ManyToManyField(
        "products.Product",
        through="favorites.FavoriteProduct",
        related_name="favorite_products",
    )

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="favorite"
    )


class FavoriteProduct(models.Model):
    class Meta:
        ordering = ["id"]

    favorite = models.ForeignKey(
        "favorites.Favorite", on_delete=models.CASCADE, related_name="favorites_pivo"
    )

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="product_pivo"
    )

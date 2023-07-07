from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import FavoriteProduct, Favorite
from products.serializers import ProductSerializer


class FavoritesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = ("id", "favorite", "product")
        read_only_fields = ["favorite"]

    def create(self, validated_data):
        favorites, created = Favorite.objects.get_or_create(user=validated_data["user"])
        favorite_add = FavoriteProduct.objects.filter(
            favorite=favorites, product=validated_data["product"]
        ).first()

        validated_data.pop("user", None)

        if validated_data["product"].stock == 0:
            raise ValidationError({"error": "Insufficient stock product!"})

        return FavoriteProduct.objects.create(favorite=favorites, **validated_data)

    def update(self, instance, validated_data):
        instance.save()

        return instance


class FavoriteListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = FavoriteProduct
        fields = ("id", "favorite", "product")
        read_only_fields = ["favorite"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ("id", "favorites_products", "user")
        depth = 1
        extra_kwargs = {"user": {"read_only": True}}

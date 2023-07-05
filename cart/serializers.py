from rest_framework import serializers
from .models import Cart, CartProduct
from products.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ("id", "cart", "product")
        read_only_fields = ["cart"]

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data["user"])
        cart_product = CartProduct.objects.filter(
            cart=cart, product=validated_data["product"]
        ).first()

        validated_data.pop("user", None)

        if validated_data["product"].stock == 0:
            raise ValidationError({"error": "no stock product!"})

        return CartProduct.objects.create(cart=cart, **validated_data)

    def update(self, instance, validated_data):
        instance.save()

        return instance


class CartProductListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ("id", "cart", "product")
        read_only_fields = ["cart"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            "id",
            "cart_products",
            "user",
        )
        depth = 1
        extra_kwargs = {"user": {"read_only": True}}

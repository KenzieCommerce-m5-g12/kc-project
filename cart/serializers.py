from rest_framework import serializers
from .models import Cart, CartProduct
from products.serializers import ProductSerializer
from users.models import User


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


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Cart
        fields = (
            "id",
            "cart_products",
            "user",
        )
        depth = 1

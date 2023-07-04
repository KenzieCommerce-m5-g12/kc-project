from rest_framework import serializers
from products.models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "url",
            "description",
            "stock",
            "user",
        ]

        depth = 1
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

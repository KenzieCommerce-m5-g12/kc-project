from rest_framework import serializers
from products.models import Product
from users.serializers import UserSerializerInProduct


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializerInProduct(read_only=True)

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
            "is_available",
            "user",
        ]

        depth = 1
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data):
        for key, value in validated_data.items():
            if key == "stock":
                if value < 1:
                    print(instance.is_available)
                    print("ok")
                    instance.is_available = False
                else:
                    instance.is_available = True
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

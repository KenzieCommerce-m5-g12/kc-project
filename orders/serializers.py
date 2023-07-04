from rest_framework import serializers
from .models import Orders
from products.serializers import ProductSerializer


class OrdersSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = ["id", "status", "products", "user", "createdAt"]

    def get_user(self, obj):
        return {"id": obj.user.id, "username": obj.user.username}

    def get_products(self, obj):
        product_serializer = ProductSerializer(obj.products.all(), many=True)
        for product in product_serializer.data:
            product.pop("user", None)
            product.pop("stock", None)
        return product_serializer.data

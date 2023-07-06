from rest_framework import serializers
from .models import Orders
from products.serializers import ProductSerializer
from users.serializers import UserSerializer, UserSerializerInProduct
from users.models import User


class OrdersSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializerInProduct(read_only=True)

    class Meta:
        model = Orders
        fields = ["id", "status", "products", "user", "createdAt"]

    def get_user(self, obj: User):
        return {"id": obj.user.id, "username": obj.user.username}

    def get_products(self, obj):
        product_serializer = ProductSerializer(obj.products.all(), many=True)
        for product in product_serializer.data:
            product.pop("user", None)
            product.pop("stock", None)
        return product_serializer.data

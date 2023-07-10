from rest_framework import serializers
from .models import Orders
from products.serializers import ProductSerializer, ProductInOrderSerializer
from users.serializers import UserSerializerInProduct
from products.models import Product


class OrdersSerializer(serializers.ModelSerializer):
    products = ProductInOrderSerializer(many=True, read_only=True)
    user = UserSerializerInProduct(read_only=True)

    class Meta:
        model = Orders
        fields = ["id", "status", "products", "user", "seller_id", "createdAt"]


from rest_framework import serializers
from .models import Orders
from products.serializers import ProductSerializer, ProductInOrderSerializer
from users.serializers import UserSerializerInProduct
from products.models import Product


class OrdersSerializer(serializers.ModelSerializer):
    products = ProductInOrderSerializer(many=True, read_only=True)
    user = UserSerializerInProduct(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Orders
        fields = ["id", "status", "products", "user", "seller_id", "total", "createdAt"]

    total_price = 0

    def get_total(self, obj: Product):
        product_serializer = ProductSerializer(obj.products.all(), many=True)
        for product in product_serializer.data:
            self.total_price += float(product["price"])
        return self.total_price

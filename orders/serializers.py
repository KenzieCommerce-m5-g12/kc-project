from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    """products = ProductsSerializer(many=True)
    user = UserSerializer()"""

    class Meta:
        model = Orders
        fields = ["id", "products", "user", "createdAt"]

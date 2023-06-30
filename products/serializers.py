from rest_framework import serializers
from products.models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
        extra_kwargs = {"user": {"read_only": True}}

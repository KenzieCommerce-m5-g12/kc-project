from rest_framework import serializers
from .models import Cart
from users.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = [
            "id",
            "name",
            "category",
            "url",
            "price",
            "stock",
            "user",
        ]

from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "country", "state", "city", "road"]

from rest_framework import serializers
from address.models import Address 


class AddressSerializer(serializers.Serializer):
  class Meta:
    model = Address
    field = ["id", "country", "state" "city", "road", "user_id"]

  def create(self, validated_data):
    return Address.create(**validated_data)
  
  def update(self, instance, validated_data):
    for key, value in validated_data.items():
      setattr(instance, key, value)
  
    instance.save()

    return instance
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User
from address.serializers import AddressSerializer
from address.models import Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "isAdmin", "address"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    address = AddressSerializer()

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")

        address = Address.objects.create(**address_data)

        if validated_data["isAdmin"]:
            return User.objects.create_superuser(**validated_data, address=address)

        return User.objects.create_user(**validated_data, address=address)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

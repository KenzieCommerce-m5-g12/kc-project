from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User
from address.serializers import AddressSerializer
from address.models import Address
from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "isAdmin", "address", "typeUser"]
        extra_kwargs = {"password": {"write_only": True}, "isAdmin": {"default": False}}

    address = AddressSerializer()

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")

        address = Address.objects.create(**address_data)

        if validated_data["isAdmin"]:
            validated_data["typeUser"] = "admin"

        if validated_data["isAdmin"]:
            return User.objects.create_superuser(**validated_data, address=address)

        return User.objects.create_user(**validated_data, address=address)

    def update(self, instance, validated_data):
        try:
            Product.objects.get(user_id=instance.id)

            type_user = "seller"
        except:
            type_user = "user"

        instance_user = self.context["request"].user

        if  instance_user.isAdmin == False and validated_data["typeUser"] == "admin":
            validated_data["typeUser"] = instance_user.typeUser


        for key, value in validated_data.items():
            if key == "typeUser" and value == "admin":
                instance.isAdmin = True
            else:
                instance.isAdmin = False
            if key == "isAdmin" and value == True:
                instance.typeUser = "admin"
            else:
                instance.typeUser = type_user
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class UserSerializerInProduct(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

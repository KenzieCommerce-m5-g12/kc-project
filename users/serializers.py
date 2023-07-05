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
            validated_data["typeUser"] = "Admin"

        if validated_data["isAdmin"]:
            return User.objects.create_superuser(**validated_data, address=address)

        return User.objects.create_user(**validated_data, address=address)

    def update(self, instance, validated_data):
        try:
            Product.objects.get(user_id=instance.id)

            type_user = "Seller"
        except:
            type_user = "User"

        instance_user = self.context["request"].user

        if  instance_user.isAdmin == False and validated_data["typeUser"] == "Admin":
            validated_data["typeUser"] = instance_user.typeUser


        for key, value in validated_data.items():
            if key == "typeUser" and value == "Admin":
                instance.isAdmin = True
            else:
                instance.isAdmin = False
            if key == "isAdmin" and value == True:
                instance.typeUser = "Admin"
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


class UserSalesSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ["username", "email", "address"]

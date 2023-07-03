from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "isAdmin", "address"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    email: serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data: dict) -> User:
        if validated_data["isAdmin"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

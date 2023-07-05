from rest_framework import permissions
from rest_framework.views import View
from .models import Orders


class CanChangeOrderStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated:
            if user.typeUser == "Seller":
                return obj.user == user
        return False

from rest_framework import permissions
from rest_framework.views import Request, View
from products.models import Product


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        if request.method == "GET":
            return True

        return obj.user == request.user or request.user.is_superuser


class IsSeller(permissions.BasePermission):
    message = "Only sellers can post product. Change your typeUser to 'seller'"

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.typeUser == "user":
                return False
        return True

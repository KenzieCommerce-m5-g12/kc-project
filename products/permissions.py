from rest_framework import permissions
from rest_framework.views import Request, View
from products.models import Product


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        return obj.user == request.user or request.user.is_superuser

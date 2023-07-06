from rest_framework import permissions


class CanChangeOrderStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated:
            if user.typeUser == "seller" or user.typeUser == "admin":
                return obj.user == user
        return False

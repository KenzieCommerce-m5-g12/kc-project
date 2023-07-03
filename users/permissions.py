from rest_framework import permissions


class MyCustomUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        if obj.username == request.user.username:
            return True

        return request.user.is_superuser


class MyCustomUserGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return False

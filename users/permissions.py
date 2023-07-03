from rest_framework import permissions


class MyCustomUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username:
            return True

        return request.user.is_superuser


class MyCustomUserGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True

        if request.user.is_superuser:
            return True

        return False

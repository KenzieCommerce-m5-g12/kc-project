from rest_framework import permissions


class MyCustomUserPermission(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method == permissions.SAFE_METHODS and request.user.is_authenticated:
      return True
    if obj.username == request.user.username:
      return True
        
    return request.user.is_superuser
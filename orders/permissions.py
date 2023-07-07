from rest_framework import permissions
from orders.models import Orders


class CanChangeOrderStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Orders):
        user = request.user
        print(user.id)
        print(obj.seller_id)
        if (user.typeUser == "seller" or user.typeUser == "admin") and obj.seller_id==user.id:
            return True
        return False

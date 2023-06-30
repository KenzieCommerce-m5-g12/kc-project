from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CanChangeOrderStatus
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import *
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework.response import Response


class OrderListCreateView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated, CanChangeOrderStatus]

    def perform_update(self, serializer):
        instance = self.get_object()
        status = self.request.data.get("status")
        instance.status = status
        instance.save()

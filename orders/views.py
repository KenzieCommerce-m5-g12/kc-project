from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .permissions import CanChangeOrderStatus
from rest_framework.generics import *
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework.views import Response, status


class OrderListCreateView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        products = self.request.data.get("products", [])
        order = serializer.save(user=self.request.user)
        if products:
            for product_id in products:
                product = get_object_or_404(Product, id=product_id)
                order.products.add(product)
            order.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CanChangeOrderStatus]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if "status" in serializer.validated_data:
            previous_status = instance.status
            instance.status = serializer.validated_data["status"]
            instance.save()

            # Verifica se o status foi alterado
            if previous_status != instance.status:
                # Lógica para enviar o e-mail
                subject = "Atualização do status do pedido"
                message = (
                    f"O status do seu pedido foi atualizado para: {instance.status}"
                )
                from_email = settings.EMAIL_HOST_USER
                to_email = instance.user.email
                send_mail(subject, message, from_email, [to_email])

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

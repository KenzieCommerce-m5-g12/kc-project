from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from products.models import Product
from .permissions import CanChangeOrderStatus
from rest_framework.generics import *
from orders.models import Orders
from orders.serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework.views import Response, status
from rest_framework import serializers


class OrderListCreateView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        cart = get_object_or_404(Cart.objects.filter(user=user))

        product_ids = cart.products_cart.values_list("id", flat=True)

        if product_ids:
            serializer.validated_data["products"] = product_ids

            order = serializer.save(user=user)

            for product_id in product_ids:
                product = get_object_or_404(Product, id=product_id)
                if product.stock < 1:
                    raise ValidationError(
                        "Insufficient stock for product: {}".format(product.name)
                    )
                product.stock -= 1
                product.save()

                cart.products_cart.remove(product)

            cart.products_cart.clear()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise serializers.ValidationError(
                "O carrinho está vazio. Adicione produtos antes de criar um pedido."
            )


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

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Cart, CartProduct
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CartProductSerializer, CartProductListSerializer


class CartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GetCartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductListSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart.objects.filter(user=self.request.user))
        cart_products = CartProduct.objects.filter(cart=cart)
        return cart_products

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CartDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

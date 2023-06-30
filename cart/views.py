from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOnwer


class CartView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOnwer]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

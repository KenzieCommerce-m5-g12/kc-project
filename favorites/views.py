from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Favorite, FavoriteProduct
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import FavoritesProductSerializer, FavoriteListSerializer


class FavoritesView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoritesProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FavoritesListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteListSerializer

    def get_queryset(self):
        favorites = get_object_or_404(Favorite.objects.filter(user=self.request.user))
        data_products = FavoriteProduct.objects.filter(favorite=favorites)
        return data_products

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FavoritesDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoritesProductSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

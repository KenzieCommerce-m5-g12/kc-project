from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductView(generics.ListCreateAPIView):
    """
    As permissões são as padrões, nao são as específicas da regra de negócio.
    Implementar depois.
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_name = self.request.query_params.get("product")
        if product_name:
            queryset = Product.objects.filter(name__icontains=product_name)
            return queryset

        product_category = self.request.query_params.get("category")
        if product_category:
            queryset = Product.objects.filter(category__icontains=product_category)
            return queryset

        product_id = self.request.query_params.get("id")
        if product_id:
            queryset = Product.objects.filter(id=product_id)
            return queryset
        
        return super().get_queryset()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

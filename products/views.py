from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.permissions import IsOwnerOrAdmin
from drf_spectacular.utils import extend_schema


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

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        operation_id="Deleta Product",
        responses={204: ProductSerializer},
        description="Delete product by id",
        summary="Delete by id",
        tags=["Product"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        operation_id="Updated Product",
        responses={200: ProductSerializer},
        description="Updated product by id",
        summary="Updated by id",
        tags=["Product"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

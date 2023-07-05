from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from users.permissions import MyCustomUserPermission, MyCustomUserGetPermission

from products.models import Product
from products.serializers import ProductInSalesSerializer

# Create your views here.


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomUserGetPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailview(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"


class LoginView(TokenObtainPairView):
    pass


class UserSalesView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Product.objects.all()
    serializer_class = ProductInSalesSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.filter(user_id=request.user.id)
        return super().get(request, *args, **kwargs)

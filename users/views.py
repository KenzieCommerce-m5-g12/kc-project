from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from users.permissions import MyCustomUserPermission, MyCustomUserGetPermission

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


class LoginView(TokenObtainPairView):
    pass

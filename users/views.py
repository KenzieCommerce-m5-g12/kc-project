from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer

# Create your views here.

class UserView(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
    

class UserDetailview(RetrieveUpdateDestroyAPIView):
  authentication_classes = [JWTAuthentication]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
  pass
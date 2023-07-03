from rest_framework.generics import CreateAPIView
from address.serializers import AddressSerializer
from address.models import Address

# Create your views here.

class AddressView(CreateAPIView):
  queryset = Address
  serializer_class = AddressSerializer

  def perform_create(self, serializer):
    return serializer.save(user=self.request.user)
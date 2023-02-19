from rest_framework.viewsets import ModelViewSet
from customer_service.models import CustomerService
from customer_service.serializer import RequestCustomerServiceSerializer, ResponseCustomerServiceSerializer
from customer_service.permissions import AttendantsPermission, ClientPermission
from users.permissions import IsAuthenticated

class CustomerServiceViewSet(ModelViewSet):
  queryset = CustomerService.objects.all()
 
  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = [IsAuthenticated]
    elif self.action == 'create':
      print(self.request)
      permission_classes = [IsAuthenticated, ClientPermission]
    else:
      permission_classes = [IsAuthenticated, AttendantsPermission]
    return [permission() for permission in permission_classes]

  def get_serializer_class(self):
    if self.request.method == "GET":
      return ResponseCustomerServiceSerializer

    return RequestCustomerServiceSerializer


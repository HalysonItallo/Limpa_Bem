from rest_framework.viewsets import ModelViewSet
from customer_service.models import CustomerService
from customer_service.serializer import CustomerServiceSerializer
from customer_service.permissions import AttendantsPermission, ClientPermission
from users.permission import IsAuthenticated

class CustomerServiceViewSet(ModelViewSet):
  queryset = CustomerService.objects.all()
  serializer_class = CustomerServiceSerializer

  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = [IsAuthenticated]
    elif self.action == 'create':
      permission_classes = [ClientPermission]
    else:
      permission_classes = [IsAuthenticated, AttendantsPermission]
    return [permission() for permission in permission_classes]


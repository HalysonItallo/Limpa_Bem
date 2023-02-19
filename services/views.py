from rest_framework.viewsets import ModelViewSet
from services.models import Service
from services.serializer import ServiceSerializer
from users.permissions import IsAuthenticated
from services.permissions import ManagerPermission

class ServiceViewSet(ModelViewSet):
  queryset = Service.objects.all()
  serializer_class = ServiceSerializer

  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = []
    else:
      permission_classes = [IsAuthenticated, ManagerPermission]
    return [permission() for permission in permission_classes]


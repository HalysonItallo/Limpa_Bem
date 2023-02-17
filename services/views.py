from rest_framework.viewsets import ModelViewSet
from services.models import Service
from services.permission import ManagerPermission, AllUsersPermission
from services.serializer import ServiceSerializer


class ServiceManagerViewSet(ModelViewSet):
  permission_classes = [ManagerPermission]

  queryset = Service.objects.all()
  serializer_class = ServiceSerializer

  def perform_create(self, serializer):
    serializer.save()


class ServiceAllUsersViewSet(ModelViewSet):
  permission_classes = [AllUsersPermission]

  queryset = Service.objects.all()
  serializer_class = ServiceSerializer

  def perform_create(self, serializer):
    serializer.save()
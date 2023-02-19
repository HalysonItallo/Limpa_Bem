from rest_framework import viewsets
from status.models import Status
from status.serializer import StatusSerializer
from users.permissions import IsAuthenticated
from status.permissions import ManagerPermission

class StatusViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]

  queryset = Status.objects.all()
  serializer_class = StatusSerializer  


  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list' or self.action == 'retrieve':
      permission_classes = [IsAuthenticated]
    else:
      permission_classes = [IsAuthenticated, ManagerPermission]
    return [permission() for permission in permission_classes]




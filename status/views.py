from rest_framework import viewsets
from status.models import Status
from status.serializer import StatusSerializer
from status.permission import AttendantPermission

class StatusAttendantViewSet(viewsets.ModelViewSet):
  permission_classes = [AttendantPermission]

  queryset = Status.objects.all()
  serializer_class = StatusSerializer  

  def perform_create(self, serializer):
    serializer.save()




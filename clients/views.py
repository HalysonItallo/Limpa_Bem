from rest_framework import viewsets
from clients.models import Client
from clients.serializer import ClientSerializer
from clients.permission import AttendantPermission

class ClientAttendantViewSet(viewsets.ModelViewSet):
  permission_classes = [AttendantPermission]

  queryset = Client.objects.all()
  serializer_class = ClientSerializer  

  def perform_create(self, serializer):
    serializer.save()




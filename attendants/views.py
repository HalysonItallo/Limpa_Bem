from rest_framework import viewsets
from attendants.models import Attendant
from attendants.serializer import AttendantSerializer
from attendants.permission import MenagerPermission

class AttendantManagerViewSet(viewsets.ModelViewSet):
  permission_classes = [MenagerPermission]

  queryset = Attendant.objects.all()
  serializer_class = AttendantSerializer

  def perform_create(self, serializer):
    serializer.save()



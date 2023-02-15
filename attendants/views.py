from rest_framework import viewsets
from attendants.models import Attendant
from attendants.serializer import AttendantSerializer

class AttendantViewSet(viewsets.ModelViewSet):
  queryset = Attendant.objects.all()
  serializer_class = AttendantSerializer  



from rest_framework import viewsets
from status.models import Status
from status.serializer import StatusSerializer

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer  



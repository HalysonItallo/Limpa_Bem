from rest_framework import viewsets
from services.models import Service
from services.serializer import ServiceSerializer
from rest_framework.permissions import IsAuthenticated

class ServicesViewSet(viewsets.ModelViewSet):
  queryset = Service.objects.all()
  serializer_class = ServiceSerializer  



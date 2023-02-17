from rest_framework.viewsets import ModelViewSet
from customer_service.permissions import HelperPermission
from customer_service.models import CustomerService
from customer_service.serializer import CustomerServiceSerializer
from customer_service.permissions import AttendantsPermission


class CustomerServiceHelperViewSet(ModelViewSet):
  permission_classes = [HelperPermission]

  queryset = CustomerService.objects.all()
  serializer_class = CustomerServiceSerializer

  def perform_create(self, serializer):
    serializer.save()

class CustomerServiceAttendantViewSet(ModelViewSet):
  permission_classes = [AttendantsPermission]

  queryset = CustomerService.objects.all()
  serializer_class = CustomerServiceSerializer

  def perform_create(self, serializer):
    serializer.save()
    
  
  

  
  
  




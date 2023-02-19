from rest_framework import serializers
from customer_service.models import CustomerService
from users.serializer import PersonSerializer
from services.serializer import ServiceSerializer
from status.serializer import StatusSerializer

class ResponseCustomerServiceSerializer(serializers.ModelSerializer):  
  client = PersonSerializer()
  service = ServiceSerializer()
  status = StatusSerializer()
  attendant = PersonSerializer()
  helper = PersonSerializer()

  class Meta:
    model = CustomerService
    exclude = ()
    
class RequestCustomerServiceSerializer(serializers.ModelSerializer):  

  class Meta:
    model = CustomerService
    exclude = ()


  







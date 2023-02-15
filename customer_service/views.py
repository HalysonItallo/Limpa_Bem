from customer_service.models import CustomerService
from customer_service.serializer import CustomerServiceSerializer
from rest_framework.response import Response


def GetAllCustomerService(resquest, format=None):
  return Response(CustomerServiceSerializer.getAllCustomerService()) 
  




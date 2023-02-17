from rest_framework import serializers
from customer_service.models import CustomerService

class CustomerServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerService
    fields = ('amount','will_carried_at')






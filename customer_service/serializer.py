from rest_framework import serializers
from customer_service.models import CustomerService

class CustomerServiceSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  service_id = serializers.DecimalField(required = True, max_digits=10, decimal_places=0)
  attendant_id = serializers.DecimalField(required = True, max_digits=10, decimal_places=0)
  responsible_helper = serializers.CharField(required = True)
  amount = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)
  type_payment = serializers.CharField(required=True)
  created_at = serializers.DateTimeField()
  will_carried_at = serializers.DateTimeField()
  status_id = serializers.DecimalField(required = True, max_digits=10, decimal_places=0)
  client_id = serializers.DecimalField(required = True, max_digits=10, decimal_places=0)


  def create(self, validated_data):
    return CustomerService.objects.create(**validated_data)

  def getAllCustomerService():
    return CustomerService.objects.all()

  def update(self, instance, validated_data):
    instance.status_id = validated_data.get('status_id', instance.status_id)
    instance.save()
    return instance






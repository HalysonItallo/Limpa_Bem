from django.db import models
from services.models import Service
from status.models import Status
from clients.models import Client

class CustomerService(models.Model):
  service_id = models.ForeignKey(
    Service, 
    on_delete=models.SET_NULL, 
    default=1, 
    null=True,
  )
  responsible_attendant = models.CharField(max_length=30)
  responsible_helper = models.CharField(max_length=30)
  amount = models.DecimalField(max_digits=10,decimal_places=2)
  type_payment = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now=True)
  will_carried_at = models.DateTimeField()
  status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, default=1, null=True)
  client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
  
  def __str__(self):
    return self.responsible_attendant

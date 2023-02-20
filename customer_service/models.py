from django.db import models
from services.models import Service
from status.models import Status
from users.models import Person


class CustomerService(models.Model):
  service = models.ForeignKey(
    Service, 
    on_delete=models.DO_NOTHING, 
  )
  attendant = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='attendant', null=True)
  helper = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='helper', null=True)
  amount = models.DecimalField(max_digits=5,decimal_places=2, null=True)
  type_payment = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now=True)
  will_carried_at = models.DateTimeField()
  status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=1)
  client = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='client')
  
  def __str__(self):
    return self.created_at

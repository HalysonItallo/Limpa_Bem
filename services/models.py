from django.db import models

class Service(models.Model):
  name = models.CharField(max_length=30)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  isAvailable = models.BooleanField()

  def __str__(self) -> str:
    return self.name

    
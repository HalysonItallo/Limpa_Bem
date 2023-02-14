from django.db import models

class Client(models.Model): 
  name = models.CharField(max_length=30)
  cellphone = models.CharField(max_length=12)
  adress = models.CharField(max_length=30)

  def __str__(self):
    return self.name

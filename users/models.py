from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
  cellphone = models.CharField(max_length=12)
  adress = models.CharField(max_length=30)
  
  def __str__(self) -> str:
    return self.first_name



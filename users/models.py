from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class Person(AbstractUser):
  cellphone = models.CharField(max_length=12)
  adress = models.CharField(max_length=30)
  
  def __str__(self) -> str:
    return self.first_name

  def save(self, *args, **kwargs):
    if self.password and not self.password.startswith('pbkdf2_sha256'):
      self.password = make_password(self.password)
    super().save(*args, **kwargs)



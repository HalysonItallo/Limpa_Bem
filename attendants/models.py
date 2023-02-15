from django.db import models

class Attendant(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


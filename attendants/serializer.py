from rest_framework import serializers
from attendants.models import Attendant

class AttendantSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Attendant
    fields = ['name', 'id',]

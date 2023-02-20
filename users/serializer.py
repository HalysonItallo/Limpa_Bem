from rest_framework.serializers import ModelSerializer, CharField
from  django.contrib.auth import get_user_model

User = get_user_model()

class PersonSerializer(ModelSerializer):
  group_name = CharField(source='groups.first.name')
  class Meta: 
    model = User
    fields = ('id', 'email', 'username', "first_name", "cellphone", "adress", "password", "group_name")
    extra_kwargs = {'password': {'write_only': True}}
  

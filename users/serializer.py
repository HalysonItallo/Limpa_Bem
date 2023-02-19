from rest_framework.serializers import ModelSerializer
from  django.contrib.auth import get_user_model

User = get_user_model()

class PersonSerializer(ModelSerializer):
  class Meta: 
    model = User
    fields = ('id', 'email', 'groups', 'username', "first_name", "cellphone", "adress", "password")
    extra_kwargs = {'password': {'write_only': True}}
  
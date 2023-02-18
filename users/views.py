from rest_framework import generics
from users.serializer import PersonSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Person

class UserViewSet(ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

  



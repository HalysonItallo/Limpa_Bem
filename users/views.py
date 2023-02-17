from rest_framework import generics
from users.serializer import PersonSerializer

class CreatePerson(generics.CreateAPIView):
  serializer_class = PersonSerializer

  



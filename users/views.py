from users.serializer import PersonSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Person
from users.permission import IsAuthenticated, ClientPermission

class PersonViewSet(ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

  lookup_field = 'id'
  lookup_url_kwarg = 'pk'

  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = [IsAuthenticated]
    elif self.action == 'retrieve':
      permission_classes = [IsAuthenticated, ClientPermission]
    else:
      permission_classes = [IsAuthenticated]
    return [permission() for permission in permission_classes]


  



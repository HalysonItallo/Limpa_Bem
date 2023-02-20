from users.serializer import PersonSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import Person
from users.permissions import IsAuthenticated, ClientPermission, ManagerPermission, AttendantAndHelperPermission
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class PersonViewSet(ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer

  def perform_create(self, serializer):
    serializer.save()

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = [IsAuthenticated, ManagerPermission | AttendantAndHelperPermission]
    elif self.action == 'retrieve':
      permission_classes = [IsAuthenticated, ClientPermission]
    elif self.action == 'create':
      permission_classes = [ClientPermission]
    else:
      permission_classes = [IsAuthenticated, ManagerPermission]
    return [permission() for permission in permission_classes]



class AuthTokenView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    group_name = user.groups.all().values("name")[0]["name"]
    
    return Response({
      'token': token.key,
      'user_id': user.pk,
      'group_name': group_name
    })
  



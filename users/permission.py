from rest_framework import permissions

# Permissões dos usuários dentro de usuários

# admin django:
# pode criar um gerente

# autenticado:
# um admin pode criar um atendente
# um atendente pode listar os usuários tipo cliente
# um helper pode listar os usuários tipo cliente
# um cliente pode listar apenas ele mesmo

# não autenticado:
# pode criar um client


class ManagerPermission(permissions.BasePermission):
  allowed_methods = ['GET','POST', 'PUT', 'DELETE']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='gerente')):
      return False
    return True

class AttendantPermission(permissions.BasePermission):
  allowed_methods = ['GET',]

  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='atendente')):
      return False
    return True

class ClientPermission(permissions.BasePermission):
  allowed_methods =  ['GET']
  
  
  def has_permission(self, request, view):
    print(request.method)
    if request.method not in self.allowed_methods:
      print("olá")
      return False
    elif not(request.user and request.user.groups.filter(name='cliente')):
      print(request.user.groups)
      return False
    
    print("tem")
    return True

  def has_object_permission(self, request, view, obj):
    client_id = int(view.kwargs['pk'])
    
    print(client_id == request.user.id)
    if client_id == request.user.id:
      return True
     
    return False
  

class IsAuthenticated(permissions.BasePermission):

  def has_permission(self, request, view):
    if not request.user.is_authenticated:
      return False
    return True
  
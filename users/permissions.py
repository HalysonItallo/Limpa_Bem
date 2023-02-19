from rest_framework import permissions

class ManagerPermission(permissions.BasePermission):
  allowed_methods = ['GET','POST', 'PUT', 'DELETE']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='gerente')):
      return False
    return True

class AttendantAndHelperPermission(permissions.BasePermission):
  allowed_methods = ['GET',]

  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(
      request.user and 
      (request.user.groups.filter(name='atendente') or 
      request.user.groups.filter(name='helper'))):
      return False
    return True

class ClientPermission(permissions.BasePermission):
  allowed_methods =  ['GET', 'POST']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False

    elif request.method == 'GET':
      if not (request.user and 
      request.user.groups.filter(name='cliente')): 
        return False
    
    elif request.method == 'POST':
      if request.data['groups'][0] != 4:
        return False
    
    return True

  def has_object_permission(self, request, view, obj):
    client_id = int(view.kwargs['pk'])
    
    if client_id != request.user.id:
      return False
     
    return True


class IsAuthenticated(permissions.BasePermission):

  def has_permission(self, request, view):
    if not request.user.is_authenticated:
      return False
    return True
  
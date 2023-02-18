from rest_framework import permissions
      
class AttendantsPermission(permissions.BasePermission):
  allowed_methods = ['GET', 'POST', 'PUT']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='atendente')):
      return False

class ClientPermission(permissions.BasePermission):
  allowed_methods = ['GET', 'POST']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='cliente')):
      return False

    





  
    
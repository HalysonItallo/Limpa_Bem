from rest_framework import permissions

class ManagerPermission(permissions.BasePermission):
  allowed_methods = ['GET','POST', 'PUT', 'DELETE']
  
  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='gerente')):
      return False
    return True

  
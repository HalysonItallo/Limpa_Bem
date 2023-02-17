from rest_framework import permissions

class ManagerPermission(permissions.BasePermission):
  allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']

  def has_permission(self, request, view):
    if not request.user.is_authenticated:
      return False
    elif request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='gerente')):
      return False

    return True

class AllUsersPermission():
  allowed_methods = ['GET']

  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False

    return True
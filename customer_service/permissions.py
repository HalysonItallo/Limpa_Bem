from rest_framework import permissions

class HelperPermission(permissions.BasePermission):
  allowed_methods = ['GET']

  def has_permission(self, request, view):
    if not request.user.is_authenticated:
      return False
    elif request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='helper')):
      return False

    return True
      
class AttendantsPermission(permissions.BasePermission):
  allowed_methods = ['GET', 'POST', 'PUT ']
  
  def has_permission(self, request, view):
    if not request.user.is_authenticated:
      return False
    elif request.method not in self.allowed_methods:
      return False
    elif not(request.user and request.user.groups.filter(name='atendente')):
      return False
    
    return True





  
    
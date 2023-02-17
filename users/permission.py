class AllUsersPermission(): 
  allowed_methods = []

  def has_permission(self, request, view):
    if request.method not in self.allowed_methods:
      return False
    
    return True
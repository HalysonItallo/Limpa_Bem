from django.contrib import admin
from users.models import Person
from django.contrib.auth.admin import UserAdmin

class Gerente(UserAdmin):
  # list_display = ('id', 'role','password')
  # list_display_links = ('role', 'password')
  # search_fields = ('name',)
  pass



admin.site.register(Person, Gerente)
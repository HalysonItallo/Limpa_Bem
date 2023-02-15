from django.contrib import admin
from attendants.models import Attendant


class Gerente (admin.ModelAdmin):
  list_display = ('id','name')
  list_display_links = ('id','name')
  search_fields = ('name',)

admin.site.register(Attendant, Gerente)

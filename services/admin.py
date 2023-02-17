from django.contrib import admin
from services.models import Service

class Gerente(admin.ModelAdmin):
  list_display = ('id', 'name', 'value', 'isAvaliable')
  list_display_links = ('name', 'value', 'isAvaliable')
  search_fields = ('name',)


admin.site.register(Service, Gerente)
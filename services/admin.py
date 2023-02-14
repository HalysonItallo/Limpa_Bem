from django.contrib import admin
from services.models import Service

class Gerente(admin.ModelAdmin):
  list_display = ('id', 'name', 'value', 'isAvailable')
  list_display_links = ('name', 'value', 'isAvailable')
  search_fields = ('name',)


admin.site.register(Service, Gerente)
from django.contrib import admin
from clients.models import Client


class Gerente(admin.ModelAdmin):
  list_display = ('id', 'name', 'cellphone', 'adress',)
  list_display_links = ( 'name', 'cellphone', 'adress',)
  search_fields = ('name',)


admin.site.register(Client, Gerente)

from django.contrib import admin
from status.models import Status


class Gerente (admin.ModelAdmin):
  list_display = ('id','name')
  list_display_links = ('id','name')
  search_fields = ('name',)


admin.site.register(Status, Gerente)
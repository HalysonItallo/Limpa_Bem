from django.contrib import admin
from customer_service.models import CustomerService


class Gerente(admin.ModelAdmin):
  list_display = ('id', 'responsible_helper', 'amount', 'type_payment', 'created_at', 'will_carried_at', )
  list_display_links = ('responsible_helper', 'amount', 'type_payment', 'created_at', 'will_carried_at',)
  search_fields = ('responsible_attendant','type_payment', 'created_at', 'will_carried_at',)


admin.site.register(CustomerService, Gerente)

from django.contrib import admin
from users.models import Person
from django.contrib.auth.admin import UserAdmin

admin.site.register(Person, UserAdmin)
from django.contrib import admin
from .models import Registro


class RegistroAdmin(admin.ModelAdmin):
    model = Registro


admin.site.register(Registro, RegistroAdmin)

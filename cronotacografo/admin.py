from django.contrib import admin
from .models import Registro


class RegistroAdmin(admin.ModelAdmin):
    model = Registro
    readonly_fields = ('data',)


admin.site.register(Registro, RegistroAdmin)

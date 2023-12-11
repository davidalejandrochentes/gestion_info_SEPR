from django.contrib import admin
from .models import Sindicato, Trabajador, Map, AsambleaAfiliados

# Register your models here.
admin.site.register(Sindicato)
admin.site.register(Trabajador)
admin.site.register(Map)
admin.site.register(AsambleaAfiliados)
from django.contrib import admin
from .models import Departamento, Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
     list_display = ["codigo",
                     "nit",
                     "nombre",
                     "apellido1",
                     "apellido2",
                     "codigo_departamento"]

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre"]
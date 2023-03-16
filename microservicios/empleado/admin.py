from django.contrib import admin
from .models import Departamento, Empleado

#Se registra el modelo Empleado para poder gestionar las tablas de los empleados en Django Administration.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
     list_display = ["codigo",
                     "nit",
                     "nombre",
                     "apellido1",
                     "apellido2",
                     "codigo_departamento"]

#Se registra el modelo Departamento para poder gestionar las tablas de los departamentos en Django Administration.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre"]
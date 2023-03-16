from rest_framework import serializers
from empleado.models import Empleado, Departamento

class EmpleadoSerializer(serializers.ModelSerializer):                    #llave_foranea.atributo
    #nombre_departamento = serializers.CharField(read_only=True, source = "codigo_departamento.nombre")
    class Meta:
        model = Empleado                                                                      
        fields = ["codigo", "nit", "nombre", "apellido1", "apellido2", "codigo_departamento"]


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["codigo", "nombre", "presupuesto"]


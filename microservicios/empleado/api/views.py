from rest_framework.viewsets import ModelViewSet
from empleado.models import Empleado, Departamento
from .serializers import EmpleadoSerializer, DepartamentoSerializer

class EmpleadoApiViewSet(ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    
    def get_queryset(self):
        empleados = Empleado.objects.all()

        nit = self.request.GET.get('nit') #se obtiene el nit, en caso de que esté en la ruta como una consulta

        if nit:
            empleados = empleados.filter(nit__iexact=nit)
        
        return empleados

class DepartamentoApiViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()

    def get_queryset(self):
        departamentos = Departamento.objects.all()

        nombre = self.request.GET.get('nombre') #se obtiene el nombre, en caso de que esté en la ruta como una consulta

        if nombre:
            departamentos = departamentos.filter(nombre__iexact=nombre)
        
        return departamentos
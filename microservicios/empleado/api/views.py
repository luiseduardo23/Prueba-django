from rest_framework.viewsets import ModelViewSet
from empleado.models import Empleado, Departamento
from .serializers import EmpleadoSerializer, DepartamentoSerializer

class EmpleadoApiViewSet(ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    
    def get_queryset(self):
        empleados = Empleado.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            empleados = empleados.filter(nombre__iexact=nombre)
        
        return empleados

class DepartamentoApiViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
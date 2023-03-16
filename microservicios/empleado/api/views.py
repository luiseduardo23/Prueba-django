from rest_framework.viewsets import ModelViewSet
from empleado.models import Empleado, Departamento
from .serializers import EmpleadoSerializer, DepartamentoSerializer

class EmpleadoApiViewSet(ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

class DepartamentoApiViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
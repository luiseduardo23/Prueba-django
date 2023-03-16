from rest_framework.routers import DefaultRouter
from empleado.api.views import EmpleadoApiViewSet, DepartamentoApiViewSet

router= DefaultRouter()

#Ruta para el ViewSet del empleado
router.register(prefix="empleado", basename="empleado", viewset= EmpleadoApiViewSet)

#Ruta para el ViewSet del departamento
router.register(prefix="departamento", basename="departamento", viewset= DepartamentoApiViewSet)
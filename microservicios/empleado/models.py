from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Departamento(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, unique=True, validators=[MaxValueValidator(9999999999)])
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

    def __str__(self):
        return str(self.codigo)

class Empleado(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, unique=True, validators=[MaxValueValidator(9999999999)])
    nit = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey(Departamento, on_delete= models.PROTECT)

    def __str__(self):
        return str(self.codigo)

from django.db import models

# En el archivo models.py de la aplicación 'plan'
from django.db import models
from django.contrib.auth.models import User

class Agencia(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    logo = models.CharField(max_length=45, null=True)
    descripcion = models.CharField(max_length=45)
    fecha_disponibilidad = models.CharField(max_length=45)

class Plan(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    fecha_disponibilidad = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    img_plan = models.CharField(max_length=45, null=True)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)

class ReservasPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey('usuario.MetodoPago', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

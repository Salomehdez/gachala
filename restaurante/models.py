from django.db import models
# En el archivo models.py de la aplicación 'restaurante'
from django.db import models
from django.contrib.auth.models import User

class Restaurante(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    img_restaurante = models.CharField(max_length=45, null=True)
    descripcion = models.CharField(max_length=45)
    fecha_disponibilidad = models.CharField(max_length=45)
    n_mesas = models.CharField(max_length=45)

class Mesas(models.Model):
    n_mesas = models.CharField(max_length=45, null=True)
    capacidad_mesas = models.CharField(max_length=45, null=True)
    disponibilidad = models.CharField(max_length=45, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class ReservaRestaurante(models.Model):
    fecha_llegada = models.CharField(max_length=45, null=True)
    hora_llegada = models.CharField(max_length=45, null=True)
    metodo_pago = models.ForeignKey('usuario.MetodoPago', on_delete=models.CASCADE)
    mesas = models.ForeignKey(Mesas, on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

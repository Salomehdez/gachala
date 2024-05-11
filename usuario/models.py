from django.db import models
# En el archivo models.py de la aplicación 'usuario'
from django.db import models
from django.contrib.auth.models import User
from hotel.models import *

class Turista(models.Model):
    nombre_completo = models.CharField(max_length=45)
    cedula = models.CharField(max_length=45, unique=True)
    tel = models.CharField(max_length=45)
    edad = models.IntegerField()
    genero = models.CharField(max_length=45, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class MetodoPago(models.Model):
    tipo_de_pago = models.CharField(max_length=45)

class ReservaHotel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    habitacion = models.ForeignKey('hotel.Habitaciones', on_delete=models.CASCADE, null=True, blank=True) 
    fecha_llegada = models.CharField(max_length=45)
    fecha_salida = models.CharField(max_length=45)
    hora_llegada = models.CharField(max_length=45)
    hora_salida = models.CharField(max_length=45)
    estado = models.CharField(max_length=45, null=True, blank=True)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    reserva_hotel = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    

class UsuarioHasReservaHotel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reserva_hotel = models.ForeignKey(ReservaHotel, on_delete=models.CASCADE, primary_key=True)



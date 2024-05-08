from django.db import models
from usuario.models import *

class Hotel(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    img_hotel = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=45)
    fecha_disponibilidad = models.CharField(max_length=45)
    n_habitaciones = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class Habitaciones(models.Model):
    n_habitacion = models.CharField(max_length=45)
    capacidad_personas = models.CharField(max_length=45)
    disponibilidad = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    reserva_hotel = models.ForeignKey(ReservaHotel, on_delete=models.CASCADE)

class Ofertas(models.Model):
    habitacion = models.ForeignKey(Habitaciones, on_delete=models.CASCADE, null=True, blank=True)  
    fecha_inicio = models.CharField(max_length=45)
    fecha_finalizacion = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    ofertascol = models.CharField(max_length=45)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)  
  
    
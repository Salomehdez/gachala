from django.db import models
# En el archivo models.py de la aplicación 'hotel'
from django.db import models
from usuario.models import *

class Ofertas(models.Model):
    id_habitacion = models.CharField(max_length=45)
    fecha_inicio = models.CharField(max_length=45)
    fecha_finalizacion = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    ofertascol = models.CharField(max_length=45)

class Hotel(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    img_hotel = models.CharField(max_length=45, null=True)
    descripcion = models.CharField(max_length=45)
    fecha_disponibilidad = models.CharField(max_length=45)
    n_habitaciones = models.CharField(max_length=45)
    ofertas = models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    
class Habitaciones(models.Model):
    n_habitacion = models.CharField(max_length=45)
    capacidad_personas = models.CharField(max_length=45)
    disponibilidad = models.CharField(max_length=45)
    precio = models.CharField(max_length=45)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    reserva_hotel = models.ForeignKey(ReservaHotel, on_delete=models.CASCADE)

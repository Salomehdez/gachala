from django.shortcuts import render
from hotel.models import *
from usuario.views import *

def ver_detalle_hotel(request): 
    if request.method == 'POST':
        nombre_hotel=request.POST.get('hotel')
        hotel=Hotel.objects.get(nombre=nombre_hotel)
        hoteles = Hotel.objects.all()
    return render (request, 'detalles.html', {'hotel':hotel, 'hoteles':hoteles})




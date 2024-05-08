from django.shortcuts import render
from hotel.models import *
from restaurante.models import *
from plan.models import *

def index (request):
    hoteles = Hotel.objects.all()
    restaurantes = Restaurante.objects.all()
    agencias = Agencia.objects.all()
    return render(request, 'home.html', {'hoteles': hoteles, 'restaurantes': restaurantes, 'agencias': agencias})

def categorias (request):
    return render(request, 'categorias.html')

def detalles (request):
    return render(request, 'detalles.html')

def contacto (request):
    return render(request, 'contacto.html')
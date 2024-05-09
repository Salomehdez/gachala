from django.shortcuts import render
from hotel.models import *
from restaurante.models import *
from plan.models import *
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import render, redirect

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

def reservar (request):
    if request.method == 'POST':
        nombre_hotel=request.POST.get('hotel')
        hotel=Hotel.objects.get(nombre=nombre_hotel)
    return render (request, 'reservar.html', {'hotel':hotel})

def login (request):
    return render(request, 'login.html')

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request)
            # La autenticación fue exitosa, puedes redirigir según el tipo de usuario
            if request.user.is_staff:
                return redirect('admin:index')  # Redirige al panel de administración
            else:
                return index(request)
        else:
            return render(request, "login.html",{'mensaje': 'Error de usuario'})
        # Devuelve un HttpResponse en el caso de GET o si hubo un error en la autenticación
    return render(request, "login.html")

def register_user(request):
    fecha = datetime.now()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')

        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'El usuario ya existe'})

        # Crea el usuario
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return index(request)  

    return render(request, 'login.html')

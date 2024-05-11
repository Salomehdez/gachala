from django.shortcuts import render
from hotel.models import *
from restaurante.models import *
from usuario.models import *
from plan.models import *
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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


def reservarHotel (request):
    if request.user.username:
        if request.method == 'POST':
            nombre_hotel=request.POST.get('hotel')
            hotel=Hotel.objects.get(nombre=nombre_hotel)
        return render (request, 'reservarHotel.html', {'hotel':hotel})
    else:
        return login_view(request)

#@login_required

@login_required
def reservarRestaurante (request): 
    if request.method == 'POST':
        nombre_restaurante=request.POST.get('restaurante')
        restaurante=Restaurante.objects.get(nombre=nombre_restaurante)
    return render (request, 'reservarRestaurante.html', {'restaurante':restaurante})

@login_required
def reservarAgencia (request): 
    if request.method == 'POST':
        nombre_agencia=request.POST.get('agencia')
        agencia=Agencia.objects.get(nombre=nombre_agencia)
    return render (request, 'reservarAgencia.html', {'agencia':agencia})

@login_required
def hacer_reserva(request):
    
    if request.method == 'POST':
        usuario = User.objects.get(username=request.user.username)  # Corrige el uso de request.user
        cantidad_personas = int(request.POST.get("cantidad_personas", 0))
        hotel = request.POST.get("hotel")  # ID del hotel donde hacer la reserva
        print(hotel)
        fecha_llegada = request.POST.get("fecha_entrada")
        fecha_salida = request.POST.get("fecha_salida")
        hora_llegada = request.POST.get("hora_llegada")
        hora_salida = request.POST.get("hora_salida")
        metodo_pago_id = request.POST.get("metodo_pago")

        metodo_pago = MetodoPago.objects.get(tipo_de_pago = metodo_pago_id)
        
        hotel = Hotel.objects.get(nombre=hotel)
        habitaciones_disponibles = Habitaciones.objects.filter(hotel=hotel, disponibilidad='disponible')  # Filtra habitaciones disponibles
        
        # Ordenar habitaciones por capacidad de personas (de mayor a menor)
        habitaciones_disponibles = habitaciones_disponibles.order_by('-capacidad_personas')
        
        total_personas = cantidad_personas
        habitaciones_a_reservar = []
        
        # Seleccionar habitaciones hasta cumplir la cantidad de personas
        for habitacion in habitaciones_disponibles:
            if total_personas <= 0:
                break
            capacidad = int(habitacion.capacidad_personas)
            if capacidad <= total_personas:
                habitaciones_a_reservar.append(habitacion)
                total_personas -= capacidad
            elif total_personas <= capacidad:
                habitaciones_a_reservar.append(habitacion)
                total_personas = 0
        
        # Comprobar si todas las personas están acomodadas
        if total_personas > 0:
            # No hay suficientes habitaciones disponibles para acomodar a todas las personas
            return render(request, 'error.html', {
                'mensaje': 'No hay habitaciones suficientes para acomodar a todas las personas.'
            })
        
        # Crear las reservas
        for habitacion in habitaciones_a_reservar:

            ReservaHotel.objects.create(
                usuario=usuario,
                habitacion=habitacion,
                fecha_llegada=fecha_llegada,
                fecha_salida=fecha_salida,
                hora_llegada=hora_llegada,
                hora_salida=hora_salida,
                estado = "Pendiente",
                metodo_pago = metodo_pago
            )
            habitacion.disponibilidad = "no disponible"
            habitacion.save()
        
        # Redirigir o mostrar un mensaje de éxito
        return render(request, 'reserva_exitosa.html', {
            'mensaje': 'Reserva realizada con éxito.',
            'habitaciones': habitaciones_a_reservar
        })
    
    
    # Si no es POST, muestra el formulario de reserva
    return reservarHotel(request)



def login_view (request):
    return render(request, 'login.html')



def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request,user)
            # La autenticación fue exitosa, puedes redirigir según el tipo de usuario
            if request.user.is_staff:
                
                return redirect('admin:index')  # Redirige al panel de administración
            else:
                print("no es super usuario")
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

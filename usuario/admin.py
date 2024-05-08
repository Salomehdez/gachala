from django.contrib import admin
from .models import Turista, MetodoPago, ReservaHotel, UsuarioHasReservaHotel

@admin.register(Turista)
class TuristaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cedula', 'tel', 'edad', 'genero', 'usuario')
    search_fields = ('nombre_completo', 'cedula', 'tel', 'usuario__username')
    list_filter = ('edad', 'genero')
    raw_id_fields = ('usuario',)

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('tipo_de_pago',)
    search_fields = ('tipo_de_pago',)

@admin.register(ReservaHotel)
class ReservaHotelAdmin(admin.ModelAdmin):
    list_display = ('fecha_llegada', 'fecha_salida', 'hora_llegada', 'hora_salida', 'metodo_pago', 'reserva_hotel', 'usuario')
    search_fields = ('fecha_llegada', 'fecha_salida', 'usuario__username')
    list_filter = ('metodo_pago',)

@admin.register(UsuarioHasReservaHotel)
class UsuarioHasReservaHotelAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'reserva_hotel')
    search_fields = ('usuario__username',)

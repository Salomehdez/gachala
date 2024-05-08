from django.contrib import admin
from .models import Ofertas, Hotel, Habitaciones

@admin.register(Ofertas)
class OfertasAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_finalizacion', 'precio', 'ofertascol')
    search_fields = ('fecha_inicio', 'fecha_finalizacion')
    list_filter = ('fecha_inicio', 'fecha_finalizacion')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_disponibilidad')
    search_fields = ('nombre', 'direccion')
    list_filter = ('fecha_disponibilidad',)

@admin.register(Habitaciones)
class HabitacionesAdmin(admin.ModelAdmin):
    list_display = ('n_habitacion', 'capacidad_personas', 'disponibilidad', 'precio', 'hotel')
    search_fields = ('n_habitacion', 'disponibilidad', 'hotel__nombre')
    list_filter = ('disponibilidad',)
    raw_id_fields = ('hotel',)

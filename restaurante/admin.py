from django.contrib import admin
from .models import Restaurante, Mesas, ReservaRestaurante

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_disponibilidad')
    search_fields = ('nombre', 'direccion')
    list_filter = ('fecha_disponibilidad',)

@admin.register(Mesas)
class MesasAdmin(admin.ModelAdmin):
    list_display = ('n_mesas', 'capacidad_mesas', 'disponibilidad', 'restaurante')
    search_fields = ('n_mesas', 'restaurante__nombre')
    list_filter = ('disponibilidad',)
    raw_id_fields = ('restaurante',)

@admin.register(ReservaRestaurante)
class ReservaRestauranteAdmin(admin.ModelAdmin):
    list_display = ('fecha_llegada', 'hora_llegada', 'metodo_pago', 'mesas', 'usuario')
    search_fields = ('fecha_llegada', 'mesas__n_mesas', 'usuario__username')
    list_filter = ('metodo_pago', 'mesas__disponibilidad', 'usuario')

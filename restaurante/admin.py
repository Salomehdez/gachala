from django.contrib import admin
from .models import Restaurante, ReservaRestaurante

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_disponibilidad')
    search_fields = ('nombre', 'direccion')
    list_filter = ('fecha_disponibilidad',)

@admin.register(ReservaRestaurante)
class ReservaRestauranteAdmin(admin.ModelAdmin):
    list_display = ('fecha_llegada', 'hora_llegada', 'metodo_pago', 'usuario')
    search_fields = ('fecha_llegada', 'usuario__username')
    list_filter = ('metodo_pago', 'usuario')

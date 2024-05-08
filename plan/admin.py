from django.contrib import admin
from .models import Agencia, Plan, ReservasPlan

@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_disponibilidad')
    search_fields = ('nombre', 'direccion')
    list_filter = ('fecha_disponibilidad',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'fecha_disponibilidad', 'agencia')
    search_fields = ('nombre', 'agencia__nombre')
    list_filter = ('fecha_disponibilidad',)
    raw_id_fields = ('agencia',)

@admin.register(ReservasPlan)
class ReservasPlanAdmin(admin.ModelAdmin):
    list_display = ('plan', 'metodo_pago', 'usuario')
    search_fields = ('plan__nombre', 'usuario__username')
    list_filter = ('metodo_pago', 'usuario')

"""
URL configuration for gachala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario.views import *
from hotel.views import *

urlpatterns = [
    path('admin/login/', login_view, name='admin_login'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),
    path('detalles/', detalles, name='detalles'),
    path('contacto/', contacto, name='contacto'),
    path('ver_detalle_hotel/', ver_detalle_hotel, name='ver_detalle_hotel'),
    path('reservarHotel/', reservarHotel, name='reservarHotel'),
    path('reservarRestaurante/', reservarAgencia, name='reservarRestaurante'),
    path('reservarAgencia/', reservarAgencia, name='reservarAgencia'),
    path('custom_login/', custom_login, name='custom_login'),
    path('register_user/', register_user, name='register_user'),
    path('login/', login_view, name='login'),#hacer_reserva
    path('hacer_reserva/', hacer_reserva, name='hacer_reserva'),
]

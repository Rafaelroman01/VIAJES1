from django.urls import path
from appexcursiones.views import *

urlpatterns = [
    path('inicio/', inicio, name="proyecto-inicio"),
    path('viajes/', viajes, name="proyecto-viajes"),
    path('recreadores/', recreadores, name="proyecto-recreadores"),
    path('clientes/', clientes, name="proyecto-clientes"),
    path('proveedores/', proveedores, name="proyecto-proveedores"),
    path('documentacion/', documentacion, name="proyecto-documentacion"),
]
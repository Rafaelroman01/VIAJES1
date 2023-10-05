from django.urls import path
from appexcursiones.views import *

urlpatterns = [
    path('inicio/', inicio, name="proyecto-inicio"),
    path('viajes/', viajes, name="proyecto-viajes"),
    path('viajes/crear/', creacion_viajes, name="proyecto-viajes-crear"),
    path('recreadores/', recreadores, name="proyecto-recreadores"),
    path('recreadores/crear/', creacion_recreadores, name="proyecto-recreadores-crear"),
    path('clientes/', clientes, name="proyecto-clientes"),
    path('clientes/crear/',creacion_clientes, name="proyecto-clientes-crear"),
    path('proveedores/', proveedores, name="proyecto-proveedores"),
    path('proveedores/crear/', creacion_proveedores, name="proyecto-proveedores-crear"),
    path('documentacion/', documentacion, name="proyecto-documentacion"),
    path('documentacion/crear/', creacion_documentacion, name="proyecto-documentacion-crear"),
]
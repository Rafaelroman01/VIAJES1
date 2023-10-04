from django.urls import path
from appexcursiones.views import *

urlpatterns = [
    path('inicio/', inicio),
    #path('recreadores/', recreadores),
    #path('clientes/', clientes),
    #path('proveedores/', proveedores),
    #path('documentacion/', documentacion),
]
from django.shortcuts import render
from django.http import HttpResponse
from appexcursiones.models import *

# Create your views here.
def inicio(request):
    return render(request, "Appnuevo/base.html")
    
def viajes(request):
    return render(request, "Appnuevo/viajes.html")

def recreadores(request):
    return render(request, "Appnuevo/recreadores.html")

def clientes(request):
    return render(request, "Appnuevo/clientes.html")

def proveedores(request):
    return render(request, "Appnuevo/proveedores.html")

def documentacion(request):
    return render(request, "Appnuevo/documentacion.html")

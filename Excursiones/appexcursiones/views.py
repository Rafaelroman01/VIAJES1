from django.shortcuts import render
from django.http import HttpResponse
from appexcursiones.forms import ViajeFormulario
from appexcursiones.models import *

# Create your views here.
def inicio(request):
    return render(request, "Appnuevo/base.html")
    
def viajes(request):
    return render(request, "Appnuevo/viajes.html")

def creacion_viajes(request):
    if request.method =="POST":
        formulario = ViajeFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            
            viajes = Viajes(nombre=data["nombre"], destino=data["destino"], grupo=data["grupo"], email=data["email"])
            
            viajes.save()
    
    formulario = ViajeFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/viajes_formularios.html", contexto)

def recreadores(request):
    return render(request, "Appnuevo/recreadores.html")

def clientes(request):
    return render(request, "Appnuevo/clientes.html")

def proveedores(request):
    return render(request, "Appnuevo/proveedores.html")

def documentacion(request):
    return render(request, "Appnuevo/documentacion.html")

from django.shortcuts import render
from django.http import HttpResponse
from appexcursiones.forms import *
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
            #
            viajes = Viajes(nombre=data["nombre"], destino=data["destino"], grupo=data["grupo"], email=data["email"])
            # Guardamos el formulario
            viajes.save()
    
    formulario = ViajeFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/viajes_formularios.html", contexto)

def buscar_viajes(request):
    return render(request, "Appnuevo/busqueda_viajes.html")

def resultados_buscar_viajes(request):
    nombre_viaje= request.GET["nombre_viaje"]
    viajes = Viajes.objects.filter(nombre__icontains=nombre_viaje)
    return render(request, "Appnuevo/resultados_busquedas_viajes.html", {"viajes":viajes})

def recreadores(request):
    return render(request, "Appnuevo/recreadores.html")


def creacion_recreadores(request):
    if request.method =="POST":
        formulario = RecreadorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            recreadores = Recreadores(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            recreadores.save()
    
    formulario = RecreadorFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/recreadores_formularios.html", contexto)


def clientes(request):
    return render(request, "Appnuevo/clientes.html")


def creacion_clientes(request):
    if request.method =="POST":
        formulario = ClienteFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            clientes = Clientes(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            clientes.save()
    
    formulario = ClienteFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/clientes_formularios.html", contexto)

def proveedores(request):
    return render(request, "Appnuevo/proveedores.html")

def creacion_proveedores(request):
    if request.method =="POST":
        formulario = ProveedorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            proveedores = Proveedores(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            proveedores.save()
    
    formulario = ProveedorFormulario()
    contexto = {"formulario": formulario}  
    return render(request, "Appnuevo/proveedores_formularios.html", contexto)

def documentacion(request):
    return render(request, "Appnuevo/documentacion.html")

def creacion_documentacion(request):
    if request.method =="POST":
        formulario = DocumentacionFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            documentacion = Documentacion(nombre=data["nombre"], fechatope=data["fechatope"], entregado=data["entregado"], email=data["email"])
            # Guardamos el formulario
            documentacion.save()
    
    formulario = DocumentacionFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/documentacion_formularios.html", contexto)

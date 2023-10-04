from django.shortcuts import render
from django.http import HttpResponse
from appexcursiones.models import *

# Create your views here.
def inicio(request):
    return render(request, "Appnuevo/index.html")
    
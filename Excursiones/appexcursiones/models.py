from django.db import models

# Create your models here.

class Viajes(models.Model):
    nombre = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    grupo = models.IntegerField()
    email= models.EmailField(max_length=80)
    

class Recreadores(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
  
class Clientes(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
   

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()
    email= models.EmailField(max_length=80) 

class Documentacion(models.Model):
    nombre = models.CharField(max_length=50)
    fechatope = models.DateField()
    entregado = models.BooleanField()
    email= models.EmailField(max_length=80)

    

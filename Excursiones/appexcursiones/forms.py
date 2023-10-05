from django import forms

class ViajeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    destino= forms.CharField(max_length=50)
    grupo = forms.IntegerField()
    email= forms.EmailField(max_length=80)
    
class RecreadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    email= forms.EmailField(max_length=80)
  
class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    email= forms.EmailField(max_length=80)
   
class ProveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    email= forms.EmailField(max_length=80) 
class DocumentacionFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fechatope = forms.DateField()
    entregado = forms.BooleanField()
    email= forms.EmailField(max_length=80)

    

    
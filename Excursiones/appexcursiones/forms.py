from django import forms

class ViajeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    destino= forms.CharField(max_length=50)
    grupo = forms.IntegerField()
    email= forms.EmailField(max_length=80)
    
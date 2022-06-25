from django import forms

class NuevoProducto(forms.Form):
    marca = forms.CharField(max_length=30,label="Marca:")
    modelo = forms.CharField(max_length=30,label="Modelo:")
    precio = forms.IntegerField(min_value=0,label="Precio:")


class NuevoEmpleado(forms.Form):
    nombre      = forms.CharField(max_length=30)
    apellido    = forms.CharField(max_length=30)
    email       = forms.CharField(max_length=30,label="Email:")

    
class NuevoCliente(forms.Form):
    nombre      = forms.CharField(max_length=30)
    apellido    = forms.CharField(max_length=30)
    email       = forms.CharField(max_length=30,label="Email:") 

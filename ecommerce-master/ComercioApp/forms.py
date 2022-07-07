from django import forms

class NuevoProducto(forms.Form):
    modelo = forms.CharField(max_length=30,label="Modelo:")
    imagen = forms.CharField(max_length=400,label="Imagen:")
    marca = forms.CharField(max_length=30,label="Marca:")
    precio = forms.IntegerField(min_value=0,label="Precio:")
    

class NuevoEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre:")
    apellido = forms.CharField(max_length=30,label="Apellido:")
    email = forms.CharField(max_length=30,label="Email:")

    
    
class NuevoCliente(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre:")
    apellido = forms.CharField(max_length=30,label="Apellido:")
    email = forms.CharField(max_length=30,label="Email:")


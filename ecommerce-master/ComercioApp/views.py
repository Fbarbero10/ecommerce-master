from django.shortcuts import render
from ComercioApp.models import *

# Create your views here.

def inicio(request):

    return render(request,"comercioApp/index.html",{})  

def productos(request):
    
    productos = Producto.objects.all()  #Nos traemos todos los productos de la DB
    return render(request,"comercioApp/productos.html",{"productos":productos})

def empleados(request):
    
    return render(request,"comercioApp/empleados.html",{})

def base(request):
    return render(request,"comercioApp/base.html",{})
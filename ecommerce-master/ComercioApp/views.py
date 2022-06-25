from django.shortcuts import render, redirect
from ComercioApp.models import *
from.forms import *

# Create your views here.

def inicio(request):

    return render(request,"comercioApp/index.html",{})  

def productos(request):
    
    productos = Producto.objects.all()  #Nos traemos todos los productos de la DB
    return render(request,"comercioApp/productos.html",{"productos":productos})

def empleados(request):

    empleados = Empleados.objects.all()  #Nos traemos todos los empleados de la DB
    return render(request,"comercioApp/empleados.html",{"empleados":empleados})

def clientes(request):

    clientes = Cliente.objects.all()  #Nos traemos todos los clientes de la DB
    return render(request,"comercioApp/clientes.html",{"clientes":clientes})

def base(request):
    return render(request,"comercioApp/base.html",{})

#PARA CREAR UN PRODUCTO
def crear_producto(request):

    if request.method == "POST":

        formulario = NuevoProducto(request.POST)

        if formulario.is_valid():

            info_producto = formulario.cleaned_data

            producto = Producto(marca=info_producto["marca"], modelo=info_producto["modelo"], precio=int(info_producto["precio"]))
           
            producto.save() 

            return redirect("productos")

        else:

            return render(request,"comercioApp/crear_producto.html",{"form":formulario})

    else:

        formularioVacio = NuevoProducto()

        return render(request,"comercioApp/crear_producto.html",{"form":formularioVacio})

#PARA CREAR UN EMPLEADO
def crear_empleado(request):

    if request.method == "POST":

        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():

            info_empleado = formulario.cleaned_data

            empleado = Empleados(nombre=info_empleado["nombre"], apellido=info_empleado["apellido"], email=info_empleado["email"])
           
            empleado.save() 

            return redirect("empleados")

        else:

            return render(request,"comercioApp/crear_empleado.html",{"form":formulario})

    else:

        formularioVacio = NuevoEmpleado()

        return render(request,"comercioApp/crear_empleado.html",{"form":formularioVacio})

    #PARA CREAR UN CLIENTE
def crear_cliente(request):

    if request.method == "POST":

        formulario = NuevoCliente(request.POST)

        if formulario.is_valid():

            info_cliente = formulario.cleaned_data

            cliente = Cliente(nombre=info_cliente["nombre"], apellido=info_cliente["apellido"], email=info_cliente["email"])
            
            cliente.save() 

            return redirect("clientes")

        else:

            return render(request,"comercioApp/crear_cliente.html",{"form":formulario})

    else:

        formularioVacio = NuevoCliente()

        return render(request,"comercioApp/crear_cliente.html",{"form":formularioVacio})


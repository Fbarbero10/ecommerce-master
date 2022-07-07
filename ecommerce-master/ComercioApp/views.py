from django.shortcuts import redirect, render

from ComercioApp.models import *

from .forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def inicio(request):
    return render(request,"comercioApp/index.html",{})

def about(request):
    return render(request,"comercioApp/about.html",{})

def productos(request):
    
    productos = Productos.objects.all()  #Nos traemos todos los cursos de la DB
    return render(request,"comercioApp/productos.html",{"productos": productos})


def empleados(request):
    
    empleados = Empleados.objects.all()
    
    return render(request,"comercioApp/empleados.html",{"empleados":empleados})


def clientes(request):
    
    clientes = Clientes.objects.all()
    
    return render(request,"comercioApp/clientes.html",{"clientes":clientes})


def base(request):
    return render(request,"comercioApp/base.html",{})




def crear_producto(request):

    # post
    if request.method == "POST":

        formulario = NuevoProducto(request.POST)

        if formulario.is_valid():

            info_producto = formulario.cleaned_data
        
            producto = Productos(marca=info_producto["marca"],modelo=info_producto["modelo"],imagen=info_producto["imagen"] ,precio=int(info_producto["precio"]))

            producto.save() # guardamos en la bd
            
            return redirect("productos")

        else:

            return render(request,"comercioApp/crear_producto.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoProducto()

        return render(request,"comercioApp/crear_producto.html",{"form":formularioVacio})
    

def crear_empleado(request):

    # post
    if request.method == "POST":

        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():

            info_empleado = formulario.cleaned_data
        
            empleado = Empleados(nombre=info_empleado["nombre"],apellido=info_empleado["apellido"] ,email=info_empleado["email"])

            empleado.save() # guardamos en la bd
            
            return redirect("empleados")

        else:

            return render(request,"comercioApp/crear_empleado.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoEmpleado()

        return render(request,"comercioApp/crear_empleado.html",{"form":formularioVacio})
    
    
def crear_cliente(request):

    # post
    if request.method == "POST":

        formulario = NuevoCliente(request.POST)

        if formulario.is_valid():

            info_cliente = formulario.cleaned_data
        
            cliente = Clientes(nombre=info_cliente["nombre"],apellido=info_cliente["apellido"] ,email=info_cliente["email"])

            cliente.save() # guardamos en la bd
            
            return redirect("clientes")

        else:

            return render(request,"comercioApp/crear_cliente.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoCliente()

        return render(request,"comercioApp/crear_cliente.html",{"form":formularioVacio})
    
    
def buscar_producto(request):
        if request.method == "POST":
            
            marca = request.POST["marca"]
            productos = Productos.objects.filter(marca__icontains=marca)
            
        else:
            productos = [] #Curso.objects.all()
        return render(request,"comercioApp/busqueda_producto.html",{"productos":productos})
      
      
def ver_producto(request, producto_id):

  producto = Productos.objects.get(id=producto_id)
  
  return render(request,"comercioApp/verProducto.html",{"producto":producto})


def editar_producto(request,producto_id):

    producto = Productos.objects.get(id=producto_id)

    if request.method == "POST":

        formulario = NuevoProducto(request.POST)

        if formulario.is_valid():

            info_producto= formulario.cleaned_data

            producto.modelo = info_producto["modelo"]
            producto.marca = info_producto["marca"]
            producto.imagen = info_producto["imagen"]
            producto.precio = int(info_producto["precio"])
            producto.save()

            return redirect("productos")

    # get
    formulario = NuevoProducto(initial={"modelo":producto.modelo, "marca":producto.marca, "imagen": producto.imagen, "precio": producto.precio})

    return render(request,"comercioApp/editar_producto.html",{"form":formulario})


def eliminar_producto(request,producto_id):

    producto = Productos.objects.get(id=producto_id)

    producto.delete()

    return redirect("productos")


def editar_empleado(request,empleado_id):

    empleado = Empleados.objects.get(id=empleado_id)

    if request.method == "POST":

        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():

            info_empleado= formulario.cleaned_data

            empleado.nombre = info_empleado["nombre"]
            empleado.apellido = info_empleado["apellido"]
            empleado.email = info_empleado["email"]
            empleado.save()

            return redirect("empleados")

    # get
    formulario = NuevoEmpleado(initial={"nombre":empleado.nombre, "apellido":empleado.apellido, "email": empleado.email})

    return render(request,"comercioApp/editar_empleado.html",{"form":formulario})


def eliminar_empleado(request,empleado_id):

    empleado = Empleados.objects.get(id=empleado_id)

    empleado.delete()

    return redirect("empleados")

def editar_cliente(request,cliente_id):

    cliente = Clientes.objects.get(id=cliente_id)

    if request.method == "POST":

        formulario = NuevoCliente(request.POST)

        if formulario.is_valid():

            info_cliente= formulario.cleaned_data

            cliente.nombre = info_cliente["nombre"]
            cliente.apellido = info_cliente["apellido"]
            cliente.email = info_cliente["email"]
            cliente.save()

            return redirect("clientes")

    # get
    formulario = NuevoCliente(initial={"nombre":cliente.nombre, "apellido":cliente.apellido, "email": cliente.email})

    return render(request,"comercioApp/editar_cliente.html",{"form":formulario})

def eliminar_cliente(request,cliente_id):


    cliente = Clientes.objects.get(id=cliente_id)

    cliente.delete()

    return redirect("clientes")

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")

    form = AuthenticationForm()

    return render(request,"comercioApp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        # form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"comercioApp/register.html",{"form":form})

    form = UserCreationForm()
    # form = UserRegisterForm()

    return render(request,"comercioApp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")
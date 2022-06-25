from django.contrib import admin
from django.urls import path,include
from ComercioApp.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos,name="productos"),
    path('empleados/',empleados,name="empleados"),
    path('clientes/',clientes,name="clientes"),
    path('crearproducto/',crear_producto,name="crear_producto"),
    path('crearempleados/',crear_empleado,name="crear_empleados"),
    path('crearcliente/',crear_cliente,name="crear_cliente"),
    path('buscarproducto/',busqueda_producto,name="busqueda_producto"),
    path("base/",base)
]
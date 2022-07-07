from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path("base/",base),
    path('productos/', productos,name="productos"),
    path('empleados/',empleados,name="empleados"),
    path('clientes/',clientes,name="clientes"),
    path('about/',about,name="about"),
    path('crearproducto/',crear_producto,name="crear_producto"),
    path('crearempleado/',crear_empleado,name="crear_empleado"),
    path('crearcliente/',crear_cliente,name="crear_cliente"),
    path('buscarproducto/',buscar_producto,name='busqueda_producto'),
    path('verproducto/<producto_id>/',ver_producto, name='verproducto'),
    path("editarproducto/<producto_id>/",editar_producto,name="editarproducto"),
    path("eliminarproducto/<producto_id>/",eliminar_producto,name="eliminarproducto"),
    path("editarempleado/<empleado_id>/",editar_empleado,name="editarempleado"),
    path("eliminarempleado/<empleado_id>/",eliminar_empleado,name="eliminarempleado"),
    path("editarcliente/<cliente_id>/",editar_cliente,name="editarcliente"),
    path("eliminarcliente/<cliente_id>/",eliminar_cliente,name="eliminarcliente"),
    path('login', login_request, name="login"), 
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
]
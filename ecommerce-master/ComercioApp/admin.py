import email
from django.contrib import admin
from ComercioApp.models import *

# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'precio')
    search_fields = ('marca', 'modelo', 'precio')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')

#Link a los sitios
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)

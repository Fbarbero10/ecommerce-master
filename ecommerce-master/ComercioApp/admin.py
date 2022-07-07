from django.contrib import admin

from ComercioApp.models import *

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','email')
    search_fields = ('nombre', 'apellido''email')


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','precio','imagen')
    search_fields = ('nombre', 'marca','modelo','precio')
    
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','email')
    search_fields = ('nombre', 'apellido''email')
    

admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Productos,ProductosAdmin)
admin.site.register(Clientes,ClientesAdmin)
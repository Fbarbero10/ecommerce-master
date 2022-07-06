from operator import truediv
from django.db import models
from django.forms import CharField
from tabnanny import verbose



class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta: 
        verbose_name_plural = 'Empleados'

class Producto(models.Model):
    marca  = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    class Meta: 
        verbose_name_plural = 'Productos'

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)  #opcional

    class Meta: 
        verbose_name_plural = 'Clientes'

# Create your models here.

from tabnanny import verbose
from django.db import models

class Empleados(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True) #opcional
    
    class Meta:
        verbose_name_plural = "Empleados"


class Productos(models.Model):
    marca = models.CharField(max_length=30)
    imagen = models.CharField(max_length=400)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Productos"
    
class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True) #opcional
    
    class Meta:
        verbose_name_plural = "Clientes"

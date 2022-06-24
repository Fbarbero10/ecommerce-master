from django.contrib import admin
from django.urls import path,include
from ComercioApp.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos,name="productos"),
    path('empleados/',empleados,name="empleados"),
    path("base/",base)
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="inicio"),
    path('catalogo/',catalogo,name="catalogo"),
    path('vendedor/',vendedor,name="vendedor"),
    path('socio/',socio,name="socio"),

    #Forms de registro
    path('cliente/',cliente,name="cliente"),
    path('catalogoform/',catalogoform, name="catalogoform"),
    path('socioform/',socioform, name="socioform"),
    path('vendedorform/',vendedorform, name="vendedorform"),

    #Forms de busqueda
    path('barraconsulta/',barraconsulta, name="barraconsulta"),
    path('consultacatalogo/',consultacatalogo, name="consultacatalogo"),
]
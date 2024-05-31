from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('carrito/', carrito, name='carrito'),
    path('galeria/', galeria, name='galeria'),
    path('menu/', menu, name='menu'),
    path('pedidos/', pedidos, name='pedidos'),
]

from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('carrito/', carrito, name='carrito'),
    path('galeria/', galeria, name='galeria'),
    path('menu/', menu, name='menu'),
    path('pedidos/', pedidos, name='pedidos'),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', logout, name="logout"),
    path('addToCart/<codigo>', addToCart, name="addToCart"),
    path('borrar', borrarSesion, name="borrar")
]

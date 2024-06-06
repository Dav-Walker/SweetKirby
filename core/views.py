from django.shortcuts import render
from .models import *
from django.contrib.auth.views import logout_then_login
from .models import *

def home(request):
    return render(request, 'index.html',)

def logout(request):
    return logout_then_login(request, login_url="login")

def carrito(request):
    return render(request, 'carrito.html')

def galeria(request):
    return render(request, 'galeria.html')

def header(request):
    return render(request, 'header.html')

def menu(request):
    tortas = Producto.objects.all()
    return render(request, 'menu.html', {'tortas':tortas})

def pedidos(request):
    return render(request, 'pedidos.html')
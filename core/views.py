from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .models import *
from django.urls import reverse

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

def delToCart(request, codigo):
    carrito = request.session.get("carrito", [])
    for p in carrito:
        if p["codigo"] == codigo:
            if p["cantidad"] > 1:
                p["cantidad"] -=1
                p["total"] = p["precio"] * p["cantidad"]
            else:
                carrito.remove(p)
            break
    request.session["carrito"] = carrito
    #return redirect(to="carrito")
    return redirect(reverse('carrito')+ '#contenido') #contenido siendo donde estan los items del carrito


def addToCart(request, codigo):
    carrito = request.session.get("carrito", [])
    producto = Producto.objects.get(codigo=codigo)
    for p in carrito:
        if p["codigo"] == codigo:
            p["cantidad"] +=1
            p["total"] = p["precio"] * p["cantidad"]
            break
    else:
        carrito.append({"codigo": codigo, 
                    "nombre": producto.nombre,
                    "precio" : producto.precio, 
                    "imagen" : producto.imagen, 
                    "categoria" : producto.categoria.nombre,
                    "cantidad": 1,
                    "total": producto.precio})
    request.session["carrito"] = carrito
    print(carrito)
    return redirect(to="menu")

def borrarSesion(request):
    request.session.flush()
    return redirect(to="home")

def carrito(request):
        carrito = request.session.get("carrito", [])
        return render(request, 'carrito.html', {"carrito" : carrito})
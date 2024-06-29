from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .models import *
from django.urls import reverse
from datetime import datetime
from django.shortcuts import redirect

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
    producto = None
    for p in carrito:
        if p["codigo"] == codigo:
            producto = p
            if p["cantidad"] > 1:
                p["cantidad"] -= 1
                p["total"] = p["precio"] * p["cantidad"]
            else:
                carrito.remove(p)
            break
    
    # Actualizar el total del carrito en la sesión
    request.session["carrito"] = carrito
    request.session['items'] = sum(item['cantidad'] for item in carrito)
    
    # Recalcular el total del carrito después de eliminar el producto
    total_carrito = sum(item['total'] for item in carrito)
    request.session['total_carrito'] = total_carrito
    
    # Redirigir a la vista del carrito
    return redirect(reverse('carrito') + '#contenido')


def addToCart(request, codigo, codigo_descuento=None):
    carrito = request.session.get("carrito", [])
    producto = Producto.objects.get(codigo=codigo)
    
    # Verificar si es lunes o si se ingresó un código de descuento
    es_lunes = datetime.now().weekday() == 0  # 0 es lunes
    descuento = es_lunes or (codigo_descuento is not None)

    for p in carrito:
        if p["codigo"] == codigo:
            p["cantidad"] += 1
            p["total"] = p["precio"] * p["cantidad"]
            if descuento:
                p["total"] *= 0.9  # Aplicar 10% de descuento
            p["total"] = round(p["total"])  # Redondear el total sin decimales
            break
    else:
        total_precio = producto.precio
        if descuento:
            total_precio *= 0.9  # Aplicar 10% de descuento
        total_precio = round(total_precio)  # Redondear el total sin decimales
        carrito.append({
            "codigo": codigo, 
            "nombre": producto.nombre,
            "precio": producto.precio, 
            "imagen": producto.imagen, 
            "categoria": producto.categoria.nombre,
            "cantidad": 1,
            "total": total_precio
        })
    
    request.session["carrito"] = carrito
    request.session['items'] = sum(item['cantidad'] for item in carrito)
    
    # Calcular el total del carrito y almacenarlo en la sesión
    total_carrito = sum(item['total'] for item in carrito)
    request.session['total_carrito'] = total_carrito
    
    # Redirigir a la vista del carrito
    return redirect(to="menu")

def borrarSesion(request):
    request.session.flush()
    return redirect('home')

def carrito(request):
    carrito = request.session.get("carrito", [])
    total_carrito = request.session.get("total_carrito", 0)  # Obtener total_carrito de la sesión
    return render(request, 'carrito.html', {"carrito": carrito, "total_carrito": total_carrito})

def aplicarDescuento(request):
    if request.method == 'POST':
        codigo_promocional = request.POST.get('codigo_promocional')
        
        # Verificar si el código promocional es válido y aplicar descuento si corresponde
        if codigo_promocional == 'KingDedede':  # Colocar el codigo para realizar la validación
            carrito = request.session.get("carrito", [])
            for item in carrito:
                item['total'] *= 0.9  # Aplicar descuento del 10%
                item['total'] = round(item['total'])  # Redondear el total 
            
            # Actualizar el total del carrito en la sesión
            total_carrito = sum(item['total'] for item in carrito)
            request.session['carrito'] = carrito
            request.session['total_carrito'] = total_carrito
        
    return redirect(reverse('carrito'))
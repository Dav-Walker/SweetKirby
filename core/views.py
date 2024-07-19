from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import logout_then_login
from django.urls import reverse
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import RegistroForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    topsellers = Producto.objects.order_by('?')[:4]  # Obtener 4 productos aleatorios como topsellers
    grupo_topsellers = {
        'topseller1': topsellers[0] if len(topsellers) > 0 else None,
        'topseller2': topsellers[1] if len(topsellers) > 1 else None,
        'topseller3': topsellers[2] if len(topsellers) > 2 else None,
        'topseller4': topsellers[3] if len(topsellers) > 3 else None,
    }
    return render(request, 'index.html', grupo_topsellers)

def logout(request):
    return logout_then_login(request, login_url="login")

def carrito_view(request):
    carrito = request.session.get("carrito", [])
    total_carrito = request.session.get("total_carrito", 0)
    return render(request, 'carrito.html', {"carrito": carrito, "total_carrito": total_carrito})

def galeria(request):
    return render(request, 'galeria.html')

def header(request):
    return render(request, 'header.html')

def menu(request):
    tortas = Producto.objects.all()
    return render(request, 'menu.html', {'tortas': tortas})

def pedidos(request):
    return render(request, 'pedidos.html')

def comprar(request):
    carrito = request.session.get("carrito", [])
    total = 0 
    for p in carrito:
        total =+ p["total"]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for p in carrito:
        detalle =DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = p["codigo"])
        detalle.precio = p["precio"]
        detalle.cantidad = p["cantidad"]
        detalle.venta = venta
        detalle.save()
        request.session["carrito"] = []
    return redirect(to="carrito_view") 


def delToCart(request, codigo):
    carrito = request.session.get("carrito", [])
    es_lunes = timezone.now().weekday() == 0  # 0 es lunes
    codigo_descuento = request.session.get("codigo_descuento", None)
    descuento = es_lunes or (codigo_descuento is not None)

    for p in carrito:
        if p["codigo"] == codigo:
            if p["cantidad"] > 1:
                p["cantidad"] -= 1
                p["total"] = p["precio"] * p["cantidad"]
                if descuento:
                    p["total"] *= 0.9
                p["total"] = round(p["total"])
            else:
                carrito.remove(p)
                break  # Rompe el bucle después de eliminar el producto

    if not carrito:
        if 'codigo_descuento_aplicado' in request.session:
            del request.session['codigo_descuento_aplicado']
        # Eliminar toda la sesión si el carrito está vacío
        request.session.flush()  # Esto eliminará todos los datos de la sesión

    else:
        request.session["carrito"] = carrito
        request.session['items'] = sum(item['cantidad'] for item in carrito)

        total_carrito = sum(item['total'] for item in carrito)
        request.session['total_carrito'] = total_carrito

    return redirect(reverse('carrito_view') + '#contenido')


def addToCart(request, codigo, porciones):
    carrito = request.session.get("carrito", [])
    producto = get_object_or_404(Producto, codigo=codigo)
    
    es_lunes = timezone.now().weekday() == 0  # 0 es lunes
    descuento = es_lunes or (request.session.get('codigo_descuento') is not None)
    
    # Busca si el producto ya está en el carrito
    for p in carrito:
        if p["codigo"] == codigo and p["porciones"] == int(porciones):
            p["cantidad"] += 1
            p["total"] = p["precio"] * p["cantidad"]
            if descuento:
                p["total"] *= 0.9
            p["total"] = round(p["total"])
            break
    else:
        # Si no está en el carrito, añádelo
        precios = {
            15: producto.precio_15_porciones,
            20: producto.precio_20_porciones,
            25: producto.precio_25_porciones,
            30: producto.precio_30_porciones,
        }
        
        precio = precios.get(int(porciones), producto.precio_15_porciones)
        total = precio
        if descuento:
            total *= 0.9
        total = round(total)
        
        carrito.append({
            "codigo": codigo,
            "nombre": producto.nombre,
            "porciones": int(porciones),
            "precio": precio,
            "cantidad": 1,
            "total": total,
            "imagen": producto.imagen if producto.imagen else None,  # Añadir la URL de la imagen
        })
    
    request.session["carrito"] = carrito
    request.session['items'] = sum(item['cantidad'] for item in carrito)
    
    total_carrito = sum(item['total'] for item in carrito)
    request.session['total_carrito'] = total_carrito
    
    return redirect("carrito_view")


def borrarSesion(request):
    request.session.flush()
    return redirect('home')

@login_required
def realizar_pago(request):
    if request.method == 'POST':
        # Lógica para procesar el pago
        # ...
        
        # Limpiar el carrito después de realizar el pago
        if 'carrito' in request.session:
            del request.session['carrito']
            request.session.flush()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

def obtener_precio_porciones(request):
    if request.method == 'GET' and request.is_ajax():
        producto_id = request.GET.get('producto_id')
        porciones = request.GET.get('porciones')

        producto = get_object_or_404(Producto, id=producto_id)
        precio = 0
        if porciones == '15':
            precio = producto.precio_15_porciones
        elif porciones == '20':
            precio = producto.precio_20_porciones
        elif porciones == '25':
            precio = producto.precio_25_porciones
        elif porciones == '30':
            precio = producto.precio_30_porciones

        return JsonResponse({'precio': precio})
    
    return JsonResponse({'error': 'Solicitud no válida'}, status=400)



@csrf_exempt
def aplicarDescuento(request):
    if request.method == 'POST':
        codigo_promocional = request.POST.get('codigo_promocional')
        
        if codigo_promocional == 'KingDedede':  
            if 'codigo_descuento_aplicado' not in request.session:
                carrito = request.session.get("carrito", [])
                for item in carrito:
                    item['total'] *= 0.9  # Aplica descuento del 10%
                    item['total'] = round(item['total'])  # Redondea el total
                
                total_carrito = sum(item['total'] for item in carrito)
                request.session['carrito'] = carrito
                request.session['total_carrito'] = total_carrito
                request.session['codigo_descuento'] = codigo_promocional
                request.session['codigo_descuento_aplicado'] = True  # Marca el descuento como aplicado
                
                return JsonResponse({'success': True, 'mensaje': 'Código aplicado correctamente', 'total_carrito': total_carrito})
            else:
                return JsonResponse({'success': False, 'mensaje': 'El código promocional ya ha sido utilizado'})
        else:
            return JsonResponse({'success': False, 'mensaje': 'Código no válido'})

    return JsonResponse({'success': False, 'mensaje': 'Método no permitido'})
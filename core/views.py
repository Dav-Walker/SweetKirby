from django.shortcuts import render
from .models import *
def home(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos':productos})

def login(request):
    return render(request, 'login.html')
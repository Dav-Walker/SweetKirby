from django.contrib import admin
from .models import *


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(DetalleVenta)

from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *
from . import views

urlpatterns = [
    path('', home, name="home"),
     path('carrito/', views.carrito_view, name='carrito_view'),
    path('galeria/', galeria, name='galeria'),
    path('menu/', menu, name='menu'),
    path('pedidos/', pedidos, name='pedidos'),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', logout, name="logout"),
    path('addToCart/<str:codigo>/<int:porciones>/', addToCart, name='addToCart'),
    path('delToCart/<codigo>/', delToCart, name="delToCart"),
    path('aplicar_descuento/', aplicarDescuento, name='aplicar_descuento'),
    path('realizar_pago/', realizar_pago, name='realizar_pago'),
    path('registro/', registro, name="registro"),
    path('borrar/', borrarSesion, name="borrar")
]

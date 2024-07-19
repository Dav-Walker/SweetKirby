from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio_15_porciones = models.IntegerField()
    precio_20_porciones = models.IntegerField()
    precio_25_porciones = models.IntegerField()
    precio_30_porciones = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    def __str__(self) -> str:
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:16]



class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self) -> str:
        return str(self.id)+" "+self.producto.nombre[0:22]+" "+str(self.venta.id)

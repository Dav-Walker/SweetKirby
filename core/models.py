from django.db import models

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


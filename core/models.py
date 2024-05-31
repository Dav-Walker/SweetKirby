from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def str(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.CharField(max_length=255, blank=False)
    categoria = models.ForeignKey(to=Categoria, on_delete = models.CASCADE, null = False, default = 1 )

    def str(self):
        return self.nombre
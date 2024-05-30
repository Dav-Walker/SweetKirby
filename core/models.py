from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nombre

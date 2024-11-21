from django.db import models

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='hamburguesas/', blank=True, null=True)

    def __str__(self):
        return self.nombre


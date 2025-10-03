from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=False)
    email = models.EmailField('Email', max_length=100, blank=False)
    telefono = models.CharField('Telefono', max_length=12, blank=False)
    dirección = models.CharField('Direccion', max_length=100, blank=False)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "proveedores"
        ordering = ("nombre", "email" , "telefono", "dirección")


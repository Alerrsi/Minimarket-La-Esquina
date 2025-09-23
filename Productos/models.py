from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField("Nombre", max_length=100, blank=False, null = False)
    categoria = models.CharField("Categoria", max_length=100, blank=False, null = False)
    precio = models.FloatField("Precio", blank=False, null = False)
    stock_actual = models.PositiveIntegerField("Stock actual", blank=False, null = False)
    stock_minimo = models.PositiveIntegerField("Stock minimo", blank=False, null = False)



    def __str__(self):
        return f"{self.nombre} {self.categoria}"
    
    class Meta:
        db_table = "productos"
        ordering = ("nombre", "categoria","precio")


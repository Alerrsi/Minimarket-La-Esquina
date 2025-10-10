from django.db import models


class Categoria(models.Model):
    nombre = models.CharField("nombre", max_length=100, null=False, blank=False)

    class Meta: 
        db_table = "categorias"
        ordering = ("id",)


    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=100, blank=False, null = False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,  blank=False, null = False)
    precio = models.FloatField('Precio', blank=False, null = False)
    stock = models.PositiveIntegerField('Stock actual', blank=False, null = False)
    stock_minimo = models.PositiveIntegerField('Stock minimo', blank=False, null = False)



    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = 'productos'
        ordering = ("id", 'nombre', 'categoria','precio', "stock")


from django.db import models
import datetime
from Proveedores.models import Proveedor
from Productos.models import Producto
from Login.models import Usuario

class Compra(models.Model):
    fecha = models.DateField(verbose_name="fecha", default = datetime.datetime.now())
    total = models.FloatField(verbose_name="total", null = True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null = False)
    # de momento podrá ser null a falta de login
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True) 

    class Meta: 
        db_table = "compras"


    def __str__(self):
        return f"Fecha: {self.fecha} | Total:  {self.total}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="cantidad")
    costo_unitario = models.FloatField(verbose_name="costo unitario")

    class Meta: 
        db_table = "detalles_compras"


    def __str__(self):
        return f"{self.producto} {self.cantidad}"



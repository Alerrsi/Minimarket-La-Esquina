from django.db import models
import datetime
# Create your models here.

from Login.models import Usuario
from Productos.models import Producto

class Venta(models.Model):
    fecha = models.DateTimeField(verbose_name='fecha_venta', default=datetime.datetime.now) 
    total = models.FloatField(verbose_name='total_venta', null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table="ventas"
    def __str__(self):
        return f"Fecha: {self.fecha} | Total:  {self.total}"
    
class DetalleVenta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='cantidad_venta')

    class Meta:
        db_table = "detalles_ventas"
    
    def __str__(self):
        return f"{self.producto} {self.cantidad}"

# Create your models here.

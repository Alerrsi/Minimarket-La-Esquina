from django.db.models.signals import post_save
from django.dispatch import receiver
from Compras.models import DetalleCompra
from Ventas.models import DetalleVenta
from django.core.signals import request_finished




@receiver(post_save, sender = DetalleCompra)
def actualizarProducto(sender, created, instance: DetalleCompra, **kwagrs):
    producto = instance.producto
    producto.stock += instance.cantidad
    producto.save()


@receiver(post_save, sender = DetalleVenta)
def actualizarProductoVentas(sender, created, instance: DetalleVenta, **kwagrs):
    producto = instance.id_producto
    producto.stock -= instance.cantidad
    producto.save()
    







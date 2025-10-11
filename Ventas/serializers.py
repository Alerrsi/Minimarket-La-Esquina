from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from Productos.models import Producto
from .models import Venta, DetalleVenta

class DetalleVentaSerializer(serializers.Serializer):
    nombre_producto = serializers.CharField(read_only= True)
    producto = serializers.IntegerField(write_only = True)
    cantidad = serializers.IntegerField()

    def validate_producto(self, value):
        if not  Producto.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Producto no existe")
        
        return value
    
    def validate_cantidad(self, value):
        if not value > 0:
            raise serializers.ValidationError("La cantidad debe ser positva")
        
        return value
        
    
    def validate(self, attrs):
        precio = Producto.objects.filter(pk= attrs["producto"]).values_list("precio", flat=True)[0]

        return attrs

class VentaSerializer(serializers.Serializer):
    total = serializers.FloatField(read_only = True)
    detalle = DetalleVentaSerializer(many=True, write_only=True)

    def create(self, validated_data):
        # quitamos los productos y almacenamos en otra variable
        detalles = validated_data.pop("detalle", [])

        # calculamos el costo total de cada productos
        total_venta = 0
        
        # creamos la venta con el total de todos los producto

        venta = Venta()
        
        venta.save()
        
        for detalle in detalles:
            # Se accede al producto
            producto = Producto.objects.get(pk=detalle["producto"])
            
            # Calcular el subtotal del producto en especifo y despues sumar
            subtotal = producto.precio * detalle["cantidad"]
            total_venta += subtotal
            
            # Create DetalleVenta
            detalle_venta = DetalleVenta(
                id_venta=venta,
                id_producto=producto,
                cantidad=detalle["cantidad"],
            )
            detalle_venta.save()
        
        # Actualizar el total final.
        venta.total = total_venta
        venta.save()
        
        return venta
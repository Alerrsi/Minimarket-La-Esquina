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
    costo_unitario = serializers.FloatField()

    def validate_producto(self, value):
        if not  Producto.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Producto no existe")
        
        return value
    
    def validate_cantidad(self, value):
        if not value > 0:
            raise serializers.ValidationError("La cantidad debe ser positva")
        
        return value
        
    def validate_costo_unitario(self, value):
        if not value > 0:
            raise serializers.ValidationError("El costo unitario debe ser positvo")
        
        return value
    
    def validate(self, attrs):
        precio = Producto.objects.filter(pk= attrs["producto"]).values_list("precio", flat=True)[0]
        
        if precio <= attrs["costo_unitario"]:
            raise serializers.ValidationError("el costo unitario debe ser menor al precio de venta: {}".format(precio))

        return attrs

class VentaSerializer(serializers.Serializer):
    fecha = serializers.DateField()
    total = serializers.FloatField(read_only = True)
    productos = DetalleVentaSerializer(many=True)

    def create(self, validated_data):
        # quitamos los productos y almacenamos en otra variable
        detalles = validated_data.pop("productos", [])

        # calculamos el costo total de cada productos
        costos = [i["costo_unitario"] * i["cantidad"] for i in detalles]
        
        # creamos la venta con el total de todos los productos
        venta = Venta(
            fecha = validated_data["fecha"],
            total = sum(costos), # se suman los costos
            )
        
        venta.save()
        
        for detalle in detalles: 
            detalle_venta = DetalleVenta(
                venta = venta,
                producto = Producto.objects.get(pk= detalle["producto"]),
                cantidad = detalle["cantidad"],
                costo_unitario = detalle["costo_unitario"],
            )

            detalle_venta.save()

        return venta

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from Proveedores.serializers import ProveedorSerializer
from Proveedores.models import Proveedor
from Productos.models import Producto
from .models import Compra, DetalleCompra

class DetalleCompraSerializer(serializers.Serializer):
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
class CompraSerializer(serializers.Serializer):
    fecha = serializers.DateField()
    total = serializers.FloatField(read_only = True)
    proveedor = serializers.IntegerField()
    productos = DetalleCompraSerializer(many=True)


    

    def validate_proveedor(self, value):
        if not Proveedor.objects.filter(pk=value):
            raise serializers.ValidationError("Proveedor no existe")
        

        return value

    



    def create(self, validated_data):
        # quitamos los productos y almacenamos en otra variable
        detalles = validated_data.pop("productos", [])

        
        # calculamos el costo total de cada productos
        costos = [i["costo_unitario"] * i["cantidad"] for i in detalles]
        
        # creamos la compra con el total de todos los productos
        compra = Compra(
            fecha = validated_data["fecha"],
            total = sum(costos), # se suman los costos
            proveedor = Proveedor.objects.get(pk=validated_data["proveedor"])
            )
        
        compra.save()
        
        for detalle in detalles: 
            detalle_compra = DetalleCompra(
                compra = compra,
                producto = Producto.objects.get(pk= detalle["producto"]),
                cantidad = detalle["cantidad"],
                costo_unitario = detalle["costo_unitario"],
            )

            detalle_compra.save()

        return compra
    

    


        







    
    




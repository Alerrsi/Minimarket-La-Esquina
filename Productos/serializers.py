from rest_framework import serializers
from .models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields =  "__all__"
        read_only_fields = ("id", "nombre")






class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = "__all__"
        read_only_fields = ("id",)


    def set_context(self, context):
        self.context = context



    def validate_nombre(self, value):
        return value
    

    def validate_categoria(self, value):
        return value
    
    def validate_precio(self, value):
        if not  value > 0:
            raise serializers.ValidationError("El precio debe ser un numero positivo")
        
        return value
        

    
    def validate_stock(self, value):
        return value
    

    def validate_stock_minimo(self, value):
        return value
    

    def validate(self, attrs):
        if not  attrs["stock"] > attrs["stock_minimo"]:
            raise serializers.ValidationError("El stock debe ser mayor al stock minimo")
        
        if Producto.objects.filter(nombre = attrs["nombre"]) and self.context.get("metodo") == "create": 
            raise serializers.ValidationError("Ya existe un producto con ese nombre")

        return attrs
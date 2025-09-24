from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = '__all__'


    def validate_nombre(self, value):
        return value
    

    def validate_categoria(self, value):
        return value
    
    def validate_precio(self, value):
        if not  value > 0:
            raise serializers.ValidationError("El precio debe ser un numero positivo")
        

    
    def validate_stock(self, value):
        if not value  > self.context["stock_minimo"]:
            raise serializers.ValidationError("El stock debe ser mayor al stock minimo")
        return value
    

    def validate_stock_minimo(self, value):
        return value
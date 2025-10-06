from rest_framework import serializers
from .models import Proveedor 

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

    def validate_nombre(self, value):
        if any(not (char.isalnum() or char.isspace()) for char in value):
            raise serializers.ValidationError("El nombre no puede tener caracteres especiales.")
        
        return value
    
    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError("Ingrese un email válido")
        
        return value
    
    def validate_telefono(self,value):
        if len(value) != 12:
            raise serializers.ValidationError("Numero de telefono incorrecto")
        
        if not value.startswith('+'):
            raise serializers.ValidationError("El número debe comenzar con '+'")

        if not value[1:].isdigit():
            raise serializers.ValidationError("El número debe contener solo dígitos después del '+'")    
        
        return value
    
    def validate_dirección(self,value):
        if any(not (char.isalnum() or char.isspace()) for char in value):
            raise serializers.ValidationError("La dirección no puede tener caracteres especiales.")
     
        return value
                

from django import forms
from .models import Proveedor 

class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ejemplo: Nestle',
            'class': 'input-field',
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com',
            'class': 'input-field',
        })
    )

    direccion = forms.CharField(
        label="Dirección",
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ejemplo: Serena 951',
            'class': 'input-field',
        })
    )

    telefono = forms.CharField(
        label="Teléfono",
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ejemplo: +54 9 11 1234-5678',
            'class': 'input-field',
        })
    )

    class Meta:
        model = Proveedor 
        fields = ['nombre', 'email', 'direccion', 'telefono'] 
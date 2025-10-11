from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo electrónico",
        widget=forms.TextInput(attrs={
            "placeholder": "Ingrese su correo electrónico",
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ingrese su contraseña",
        })
    )

    class Meta:
        fields = ["username", "password"]

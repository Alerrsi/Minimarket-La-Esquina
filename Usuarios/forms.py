from django import forms
from django.core.exceptions import ValidationError
from Login.models import Usuario, Rol
import re

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        min_length=8,
        help_text="Mínimo 8 caracteres"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'direccion', 'rol', 'profile_picture']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise ValidationError("El nombre es obligatorio")
        if len(nombre) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios")
        return nombre.capitalize()

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido', '').strip()
        if not apellido:
            raise ValidationError("El apellido es obligatorio")
        if len(apellido) < 2:
            raise ValidationError("El apellido debe tener al menos 2 caracteres")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
            raise ValidationError("El apellido solo puede contener letras y espacios")
        return apellido.capitalize()

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise ValidationError("El email es obligatorio")
        
        # Validar formato de email
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValidationError("Formato de email inválido")
        
        # Verificar unicidad (excepto para el usuario actual)
        if self.instance and self.instance.pk:
            if Usuario.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError("Este email ya está registrado")
        else:
            if Usuario.objects.filter(email=email).exists():
                raise ValidationError("Este email ya está registrado")
        
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Solo validar confirmación si se está creando usuario o cambiando contraseña
        if password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden")

        return cleaned_data

class ProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={
            'class': 'input-field',
            'placeholder': 'Dejar vacío para mantener la contraseña actual'
        }),
        required=False,
        strip=False
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={
            'class': 'input-field', 
            'placeholder': 'Repetir la nueva contraseña'
        }),
        required=False,
        strip=False,
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'direccion', 'profile_picture']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Tu nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Tu apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'correo@ejemplo.com'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Tu dirección completa'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not nombre:
            raise ValidationError("El nombre es obligatorio")
        if len(nombre) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios")
        return nombre.capitalize()

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido', '').strip()
        if not apellido:
            raise ValidationError("El apellido es obligatorio")
        if len(apellido) < 2:
            raise ValidationError("El apellido debe tener al menos 2 caracteres")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
            raise ValidationError("El apellido solo puede contener letras y espacios")
        return apellido.capitalize()

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise ValidationError("El email es obligatorio")
        
        # Validar formato de email
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValidationError("Formato de email inválido")
        
        # Para el perfil, permitir que el usuario mantenga su email actual
        # sin validaciones de unicidad estrictas (ya que está editando su propio perfil)
        if self.instance and self.instance.pk:
            if Usuario.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError("Este email ya está registrado")
        
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Solo validar confirmación si se proporcionó una contraseña
        if password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden")

        # Validar fortaleza de contraseña si se proporcionó
        if password:
            if not any(char.isalpha() for char in password):
                self.add_error('password', "La contraseña debe contener al menos una letra")
            if not any(char.isdigit() for char in password):
                self.add_error('password', "La contraseña debe contener al menos un número")
            if not any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
                self.add_error('password', "La contraseña debe contener al menos un carácter especial")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Actualizar contraseña si se proporcionó
        password = self.cleaned_data.get('password')
        if password and password.strip():
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user
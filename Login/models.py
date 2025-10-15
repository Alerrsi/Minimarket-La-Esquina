from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.exceptions import ValidationError
import os, re

class Rol(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.CharField('Descripción', max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

    class Meta:
        db_table = 'roles'
        ordering = ('nombre',)

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, apellido, email, direccion, rol, password=None):
        if not nombre:
            raise ValueError("Debe ingresar un nombre")
        if not email:
            raise ValueError("Debe ingresar un correo electrónico")

        email = self.normalize_email(email)
        user = self.model(
            nombre=nombre,
            apellido=apellido,
            email=email,
            direccion=direccion,
            rol=rol,
            date_joined=timezone.now() 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, email, direccion, password):
        try:
            rol_sysadmin = Rol.objects.get(nombre='Sysadmin')
        except Rol.DoesNotExist:
            raise ValueError("El rol 'Sysadmin' no existe. Debe crearse antes de crear un superusuario.")

        user = self.create_user(
            nombre=nombre,
            apellido=apellido,
            email=email,
            direccion=direccion,
            rol=rol_sysadmin,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

def user_picture(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"profile_{instance.id}.{ext}"
    return os.path.join('profile_pictures', f"user_{instance.id}", filename)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    #Campo de foto perfil
    profile_picture = models.ImageField(
        'Foto de perfil',
        upload_to=user_picture,
        null=True,
        blank=True,
        default='profile_pictures/default_profile.png'
    )
    
    date_joined = models.DateTimeField('Fecha de registro', default=timezone.now)
    last_login = models.DateTimeField('Último acceso', null=True, blank=True)
    last_update = models.DateTimeField('Fecha de modificación', auto_now=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido", "direccion"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def clean(self):
        # Validar email
        if self.email:
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
                raise ValidationError({'email': 'Formato de email inválido'})
        
        # Validar nombre y apellido
        if self.nombre and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', self.nombre):
            raise ValidationError({'nombre': 'El nombre solo puede contener letras y espacios'})
        
        if self.apellido and not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', self.apellido):
            raise ValidationError({'apellido': 'El apellido solo puede contener letras y espacios'})

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def get_profile_picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return '/static/images/default_profile.png'
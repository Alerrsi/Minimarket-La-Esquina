from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
            rol=rol
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, email, direccion, rol, password):
        user = self.create_user(
            nombre=nombre,
            apellido=apellido,
            email=email,
            direccion=direccion,
            rol= Rol.objects.get(pk=rol),
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "apellido", "direccion", "rol"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


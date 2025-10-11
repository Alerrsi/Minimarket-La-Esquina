from django.urls import path
from Usuarios.views import Usuarioviews, UsuarioAdd, UsuarioMod, UsuarioDel

urlpatterns = [
    path("usuarios/", Usuarioviews, name = "usuario"),
    path('usuarios/add/', UsuarioAdd, name='UsuarioAdd'),
    path('usuarios/modify/<int:id>/', UsuarioMod, name='UsuarioMod'),
    path('usuarios/delete/<int:id>/', UsuarioDel, name='UsuarioDel'),

]
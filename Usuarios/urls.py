from django.urls import path
from Usuarios.views import Usuarioviews, UsuarioAdd, UsuarioMod, UsuarioDel, ViewProfile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("usuarios/", Usuarioviews, name = "usuarioViews"),
    path('usuarios/add/', UsuarioAdd, name='UsuarioAdd'),
    path('usuarios/modify/<int:id>/', UsuarioMod, name='UsuarioMod'),
    path('usuarios/delete/<int:id>/', UsuarioDel, name='UsuarioDel'),
    path('profile/', ViewProfile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
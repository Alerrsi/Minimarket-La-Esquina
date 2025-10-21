from django.urls import path
from Usuarios.views import Usuarioviews, UsuarioAdd, UsuarioMod, UsuarioDel, ViewProfile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("Usuarios/", Usuarioviews, name = "usuarioViews"),
    path('Usuarios/add/', UsuarioAdd, name='UsuarioAdd'),
    path('Usuarios/modify/<int:id>/', UsuarioMod, name='UsuarioMod'),
    path('Usuarios/delete/<int:id>/', UsuarioDel, name='UsuarioDel'),
    path('Profile/', ViewProfile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
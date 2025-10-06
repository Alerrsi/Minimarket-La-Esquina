
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Productos.urls")),
    path("", include("Proveedores.urls")),
    path("", include("Core.urls")),
    path("", include("Ventas.urls")),
    path("", include("Compras.urls"))
]
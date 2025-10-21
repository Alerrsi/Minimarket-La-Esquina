from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()


router.register("proveedores", ProveedorViewSet, basename="proveedores")

urlpatterns = [
    path("api/", include(router.urls)),
    path('Proveedores', proveedorView, name ='proveedorView'),
    path('Proveedores/formulario', proveedorForm, name="proveedorForm") ,
    path('Proveedores/formulario/<int:id>/', proveedorMod, name='editar_proveedor'),
    path('Proveedores/<int:id>/', proveedorDel, name="eliminar_proveedor")
]


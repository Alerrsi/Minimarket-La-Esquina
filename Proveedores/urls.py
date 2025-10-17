from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()


router.register("proveedores", ProveedorViewSet, basename="proveedores")

urlpatterns = [
    path("api/", include(router.urls)),
    path('proveedores', proveedorView, name ='proveedorView'),
    path('proveedores/formulario', proveedorForm, name="proveedorForm") ,
    path('proveedores/formulario/<int:id>/', proveedorMod, name='editar_proveedor'),
    path('proveedores/<int:id>/', proveedorDel, name="eliminar_proveedor")
]


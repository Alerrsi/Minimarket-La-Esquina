from django.urls import path, include
from rest_framework import routers
from .views import ProveedorViewSet




router = routers.DefaultRouter()


router.register("proveedores", ProveedorViewSet, basename="proveedores")

urlpatterns = [
    path("api/", include(router.urls))
]


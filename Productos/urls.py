from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, productosView, productosForm

# define los endpoints para los viewset
router = routers.DefaultRouter()


router.register("productos", ProductoViewSet, basename="productos")


urlpatterns = [
    path("api/", include(router.urls)),
    path("Productos", productosView, name = "productosView"),
    path("Productos/Formulario", productosForm, name = "productosForm"),
]


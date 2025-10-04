from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, CategoriaViewSet, productosView, productosForm, productosUpdate

# define los endpoints para los viewset
router = routers.DefaultRouter()


router.register("productos", ProductoViewSet, basename="productos")
router.register("categorias", CategoriaViewSet, basename="categorias")


urlpatterns = [
    path("api/", include(router.urls)),
    path("Productos", productosView, name = "productosView"),
    path("Productos/Formulario", productosForm, name = "productosForm"),
    path("Productos/Editar/<int:id>", productosUpdate, name = "productosUpdate"),
]
from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet, productoForm

# define los endpoints para los viewset
router = routers.DefaultRouter()


router.register("productos", ProductoViewSet, basename="productos")


urlpatterns = [
    path("api/", include(router.urls)),
    path("Formulario/Productos", productoForm, name = "productoForm")
]


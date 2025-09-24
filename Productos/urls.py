from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet

# define los endpoints para los viewset
router = routers.DefaultRouter()


router.register("api/productos", ProductoViewSet, basename="productos")


urlpatterns = [
    path("", include(router.urls))
]


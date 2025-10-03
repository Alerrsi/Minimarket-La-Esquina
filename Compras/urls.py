from django.urls import path
from .views import compras

urlpatterns = [
    path("Compras", compras, name = "compras")
]
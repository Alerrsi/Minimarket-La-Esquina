from django.urls import path, include
from rest_framework import routers
from .views import comprasForm, CompraApiView


urlpatterns = [
    path("api/compras", CompraApiView.as_view(), name = "compras"),
    path("Compras/Formulario", comprasForm, name = "comprasForm"),
]
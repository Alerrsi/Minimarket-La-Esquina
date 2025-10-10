from django.urls import path, include
from rest_framework import routers
from .views import comprasForm, comprasView, CompraApiView


urlpatterns = [
    path("api/compras/", CompraApiView.as_view(), name = "compras"),
    path("Compras", comprasView, name = "comprasView"),
    path("Compras/Formulario", comprasForm, name = "comprasForm"),
]
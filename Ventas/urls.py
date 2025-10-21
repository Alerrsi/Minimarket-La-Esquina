from django.urls import path, include
from rest_framework import routers
from .views import ventasView, VentaApiView, ventasForm

urlpatterns = [
    path("api/ventas", VentaApiView.as_view(), name = "ventas"),
    path("Ventas/formulario", ventasForm, name='ventasForm'),
    path("Ventas", ventasView, name="ventasView")
]
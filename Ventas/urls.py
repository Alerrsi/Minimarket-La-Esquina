from django.urls import path, include
from rest_framework import routers
from .views import ventasForm, ventasView, VentaApiView

urlpatterns = [
    path("api/ventas", VentaApiView.as_view(), name = "ventas"),
    path("Ventas", ventasView, name='ventasView'),
    path("Ventas/Formulario", ventasForm, name='ventasForm')
]
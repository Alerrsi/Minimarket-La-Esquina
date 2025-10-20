from django.urls import path, include
from rest_framework import routers
from .views import ventasView, VentaApiView, ventasForm

urlpatterns = [
    path("api/ventas", VentaApiView.as_view(), name = "ventas"),
    path("ventas/formulario", ventasForm, name='ventasForm'),
    path("ventas", ventasView, name="ventasView")
]
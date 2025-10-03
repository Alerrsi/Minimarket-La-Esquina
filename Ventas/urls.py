from django.urls import path
from .views import ventas

urlpatterns = [
    path("Ventas", ventas, name = "ventas")
]
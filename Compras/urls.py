from django.urls import path
from .views import comprasForm

urlpatterns = [
    path("Compras/Formulario", comprasForm, name = "comprasForm")
]
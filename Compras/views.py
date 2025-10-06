from django.shortcuts import render
from Proveedores.models import Proveedor
# Create your views here.

def comprasForm(request):
    return render(request, "formulario-compras.html")






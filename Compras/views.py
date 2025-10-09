from django.shortcuts import render
from Proveedores.models import Proveedor
# Create your views here.

def comprasForm(request):

    request.session.get("productos", [])
    return render(request, "formulario-compras.html")






from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views
from Proveedores.models import Proveedor
from .serializers import CompraSerializer


class CompraApiView(views.APIView):

    def post(self, request):
        serializer = CompraSerializer(data = request.data)
        if serializer.is_valid():
            print("hola")
            serializer.save()

            return Response(request.data)

        print(serializer.errors)
        return Response(serializer.errors)
    

    def get(self, request):
        compras = CompraSerializer()



def comprasForm(request):

    request.session.get("productos", [])
    return render(request, "formulario-compras.html")






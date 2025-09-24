from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response


class ProductoViewSet(viewsets.ModelViewSet):
    # conjunto de datos 
    queryset = Producto.objects.all()
    # clase que serializa los datos como json()
    serializer_class = ProductoSerializer

    # metodo de para enviar todos los registros mediante GET
    def list(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    
    # metodo para crear productos mediante POST
    def create(self, request):
        print(request.POST)
    # metodo de para enviar un solo producto mediante GET
    def retrieve(self, request, pk=None):
        pass
    # metodo de para actualizar un solo producto mediante PUT
    def update(self, request, pk=None):
        pass
    # metodo de para Aactualizar un solo producto mediante PATCH
    def partial_update(self, request, pk=None):
        pass
    # metodo para elimina un producto
    def destroy(self, request, pk=None):
        pass



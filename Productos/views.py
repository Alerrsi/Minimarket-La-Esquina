from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import viewsets, status
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response


class ProductoViewSet(viewsets.ModelViewSet):
    # conjunto de datos 
    queryset = get_list_or_404(Producto)
    # clase que serializa los datos como json()
    serializer_class = ProductoSerializer

    # metodo de para enviar todos los registros mediante GET
    def list(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    
    # metodo para crear productos mediante POST
    def create(self, request):
        # deserializampos los datos
        serializer = ProductoSerializer(data = request.data, context = {"metodo": "create"})

        # guardamos el producto si cumple con las validaciones
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("creacion")
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)
    
    # metodo de para enviar un solo producto mediante GET
    def retrieve(self, request, pk=None):
        producto = get_object_or_404(Producto, pk = pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # metodo de para actualizar un solo producto mediante PUT
    def update(self, request, pk=None):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto, data = request.data, context = {"metodo": "update"})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors)
            
    # metodo de para Aactualizar un solo producto mediante PATCH
    def partial_update(self, request, pk=None):
        pass
    # metodo para elimina un producto
    def destroy(self, request, pk=None):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return Response(status=status.HTTP_200_OK)




def productosView(request):
    return render(request, "productos.html")

def productosForm(request):
    return render(request, "formulario-productos.html")


def productosUpdate(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, "formulario-productos.html", {"producto": producto})
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required, user_passes_test
from .serializers import ProductoSerializer, CategoriaSerializer
from rest_framework.response import Response
from .models import Producto, Categoria
from .permissions import ProductoPermission


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [ProductoPermission]


    def retrieve(self, request,pk=None,  *args, **kwargs):
        categoria = get_object_or_404(Categoria, pk=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status= status.HTTP_200_OK)

class ProductoViewSet(viewsets.ModelViewSet):
    # conjunto de datos 
    queryset = Producto.objects.all()
    # clase que serializa los datos como json()
    serializer_class = ProductoSerializer
    permission_classes = [ProductoPermission]

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



@login_required
@user_passes_test(lambda x: x.rol.nombre == "Administrador" or x.rol.nombre == "Sysadmin" or x.rol.nombre == "Bodeguero")
def productosView(request):
    cantidad_productos = Producto.objects.all().count()
    disponibles = Producto.objects.filter(stock__gt = 0).count()
    stock_bajo = Producto.objects.filter(stock__lte = F("stock_minimo")).count()
    return render(request, "productos.html", {"cantidad_productos": cantidad_productos, "stock_bajo": stock_bajo, "disponibles": disponibles})


@login_required
@user_passes_test(lambda x: x.rol.nombre == "Administrador" or x.rol.nombre == "Sysadmin" or x.rol.nombre == "Bodeguero")
def productosForm(request):
    return render(request, "formulario-productos.html", {"categorias": Categoria.objects.all()})

@login_required
@user_passes_test(lambda x: x.rol.nombre == "Administrador" or x.rol.nombre == "Sysadmin" or x.rol.nombre == "Bodeguero")
def productosUpdate(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, "formulario-productos.html", {"producto": producto, "categorias": Categoria.objects.all()}) 
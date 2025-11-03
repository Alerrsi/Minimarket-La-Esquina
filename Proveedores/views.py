from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.response import Response
from rest_framework import viewsets, status
from . serializers import ProveedorSerializer
from .models import Proveedor
from .forms import ProveedorForm



class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


    def list(self, request):
        productos = Proveedor.objects.all()
        serializer = ProveedorSerializer(productos, many = True)
        return Response(serializer.data)
    
    # metodo para crear productos mediante POST
    def create(self, request):
        # deserializampos los datos
        print(request.data)
        serializer = ProveedorSerializer(data = request.data, context = {"metodo": "create"})

        # guardamos el producto si cumple con las validaciones
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("creacion")
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)
    
    # metodo de para enviar un solo producto mediante GET
    def retrieve(self, request, pk=None):
        producto = get_object_or_404(Proveedor, pk = pk)
        serializer = ProveedorSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # metodo de para actualizar un solo producto mediante PUT
    def update(self, request, pk=None):
        producto = get_object_or_404(Proveedor, pk=pk)
        serializer = ProveedorSerializer(producto, data = request.data, context = {"metodo": "update"})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors)
            
    # metodo de para Aactualizar un solo producto mediante PATCH
    def partial_update(self, request, pk=None):
        pass
    # metodo para elimina un producto
    def destroy(self, request, pk=None):
        producto = get_object_or_404(Proveedor, pk=pk)
        producto.delete()
        return Response(status=status.HTTP_200_OK)

@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def proveedorView(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def proveedorForm(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.nombre = proveedor.nombre.capitalize()  
            proveedor.direccion = proveedor.direccion.capitalize()  
            proveedor.save()  
            return redirect('proveedorView')  
    else:
        form = ProveedorForm() 
    
    return render(request, 'proveedores-formulario.html', {'form': form})

@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def proveedorMod(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedorView')  
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'proveedores-formulario.html', {'form': form})

@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def proveedorDel(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)

    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedorView')
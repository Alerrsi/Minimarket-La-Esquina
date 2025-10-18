from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required, user_passes_test
from Proveedores.models import Proveedor
from .serializers import CompraSerializer
from .models import Compra, DetalleCompra
from .permissions import CompraPermission

class CompraApiView(views.APIView):
    
    permission_classes = [CompraPermission]

    def post(self, request):
        serializer = CompraSerializer(data = request.data)
        if serializer.is_valid():
            
            serializer.save()

            return Response(request.data, status=status.HTTP_201_CREATED)

        
        return Response(serializer.errors)
    

    def get(self, request):
        
        compras = [
            {   
                "id": c.id,
                "fecha": c.fecha,
                "total": c.total,
                "proveedor": c.proveedor.id,
                "productos": 
                    [
                        {
                         "nombre_producto": d.producto.nombre,
                         "producto":d.producto.id, 
                         "cantidad":d.cantidad, 
                         "costo_unitario":d.costo_unitario
                         } 
                        for d in DetalleCompra.objects.filter(compra= c.id)
                    ]
            } 
            for c in Compra.objects.all()
        ]

        a = Compra.objects.all().values_list("fecha")
        print(a)
        
        serializer = CompraSerializer(compras, many=True)
        return Response(serializer.data)



@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def comprasForm(request):

    return render(request, "formulario-compras.html")


@login_required
@user_passes_test(lambda x: x.rol.nombre == "Bodeguero" or x.rol.nombre == "Sysadmin")
def comprasView(request):
    return render(request, "compras.html")







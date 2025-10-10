from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from Proveedores.models import Proveedor
from .serializers import CompraSerializer
from .models import Compra, DetalleCompra


class CompraApiView(views.APIView):
    

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



def comprasForm(request):
    return render(request, "formulario-compras.html")


def comprasView(request):
    return render(request, "compras.html")







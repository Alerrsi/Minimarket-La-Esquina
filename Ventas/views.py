from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from .serializers import VentaSerializer,DetalleVentaSerializer
from .models import Venta, DetalleVenta


class VentaApiView(views.APIView):
    

    def post(self, request):
        print("Request data:", request.data)  # Debug what you're receiving
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)


def ventasForm(request):
    return render(request, "formulario-ventas.html")


def ventasView(request):
    return render(request, "ventas.html")







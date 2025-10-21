from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from .permissions import VentasPermisos
from .serializers import VentaSerializer,DetalleVentaSerializer
from .models import Venta, DetalleVenta, Producto


class VentaApiView(views.APIView):
    
    permission_classes = [VentasPermisos]

    def post(self, request):
        print("Request data:", request.data)
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            venta = serializer.save()
            return Response({
                'id': venta.id,
                'total': venta.total,
                'fecha': venta.fecha
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Cajero" or x.rol.nombre == "Sysadmin")
def ventasView(request):
    # Obtener todas las ventas
    ventas = Venta.objects.all().order_by('-fecha')
    
    # Calcular estadísticas
    total_ingresos = sum(venta.total for venta in ventas if venta.total)
    promedio_venta = total_ingresos / len(ventas) if ventas else 0
    
    context = {
        'ventas': ventas,
        'total_ingresos': total_ingresos,
        'promedio_venta': promedio_venta,
    }
    
    return render(request, 'ventas.html', context)

@login_required
@user_passes_test(lambda x:x.rol.nombre == "Cajero" or x.rol.nombre == "Sysadmin")
def ventasForm(request):
    Productos = Producto.objects.all()[:8]
    context = {
        'Productos': Productos,
        'usuario_id': request.user.id
    }
    return render(request, "formulario-ventas.html", context)



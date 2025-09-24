from django.shortcuts import render
from rest_framework import viewsets



class ProductoViewSet(viewsets.ViewSet):

    # metodo de para enviar todos los registros mediante GET
    def list(self, request):
        pass
    # metodo para crear productos mediante POST
    def create(self, request):
        pass
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



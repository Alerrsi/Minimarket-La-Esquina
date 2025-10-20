from rest_framework.permissions import BasePermission, SAFE_METHODS



class VentasPermisos(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False

        roles = [0, 3]

        return request.user.rol.id in roles
    
    
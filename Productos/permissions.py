from rest_framework.permissions import BasePermission, SAFE_METHODS


class ProductoPermission(BasePermission):
    def has_permission(self, request, view):
        # Si la peticion es de tipo get deja acceder
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_anonymous:
            return False
        
        # roles que pueden acceder a la funcion
        # (SysAdmin, Administrador, Bodeguero)
        roles = [0, 1, 2]

        return request.user.rol.id in roles

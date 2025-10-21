from rest_framework.permissions import BasePermission, SAFE_METHODS


class CompraPermission(BasePermission):

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        


        roles = [0, 2]

        return request.user.rol.id in roles 
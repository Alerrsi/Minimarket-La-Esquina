from rest_framework.permissions import BasePermission


class CompraPermission(BasePermission):

    def has_permission(self, request, view):
        

        roles = [0, 2]

        return request.user.rol.id in roles
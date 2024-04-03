from rest_framework.permissions import BasePermission


class IsAdminOrCreateOnly(BasePermission):  # Permission customizada(POST para qualquer usuario , GET apenas admin)
    def has_permission(self, request, view):
        if request.method == "POST":  # Verifica se o método da requisição é POST
            return True
        return request.user and request.user.is_staff


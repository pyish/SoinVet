from rest_framework.permissions import BasePermission

class Is_Vet(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_vet_officer

class Is_Farmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_farmer

class Is_Official(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_official
    
class IsVetOrOfficial(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and
            (getattr(request.user, 'is_vet_officer', False) or getattr(request.user, 'is_official', False))
        )
class Is_Coop(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_cooperative
    

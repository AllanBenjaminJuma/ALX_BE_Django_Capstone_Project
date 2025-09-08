from rest_framework import permissions

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "client")

class IsArchitect(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.isAuthenticated and request.user.role == 'Architect')
    
class IsBookingParticipatOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        user = request.user
        if not user or not user.is_authenticated:
            return False
        
        if user.is_staff:
            return True
        
        return (hasattr(user, 'client_profile') and obj.client.user_id == user.id) or \
                (hasattr(user, 'architect__profile') and obj.architect.user_id == user.id)
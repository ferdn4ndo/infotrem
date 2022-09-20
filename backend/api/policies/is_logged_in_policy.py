from rest_framework.permissions import IsAuthenticated

from core.services.user.user_permissions_service import UserPermissionsService


class IsLoggedInPolicy(IsAuthenticated):
    def has_permission(self, request, view):
        # Always allow OPTIONS requests to ensure proper CORS checking
        if request.method == 'OPTIONS':
            return True

        service = UserPermissionsService(user=request.user)

        return service.is_logged_in()

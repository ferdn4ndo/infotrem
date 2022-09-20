from rest_framework.permissions import BasePermission, SAFE_METHODS

from core.services.user.user_permissions_service import UserPermissionsService


class IsLoggedInOrReadOnlyPolicy(BasePermission):
    """ Object-level permission to only allow everybody to read an object, but only logged users can update it. """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        service = UserPermissionsService(user=request.user)

        return service.is_logged_in()

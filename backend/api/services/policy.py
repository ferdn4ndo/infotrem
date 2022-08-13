from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AllowAll(BasePermission):
    def has_permission(self, request, view):
        return True


class IsLoggedIn(IsAuthenticated):
    def has_permission(self, request, view):
        # Always allow OPTIONS requests to ensure proper CORS checking
        if request.method == 'OPTIONS':
            return True

        return bool(request.user and request.user.is_authenticated)
    pass


class IsAdminOrDeny(BasePermission):
    """
    Object-level permission to only allow admins to read/write it.
    Assumes the model instance has an `created_by` attribute.
    """
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        return request.user and type(request.user) is not AnonymousUser and request.user.is_admin


class IsAdminOrReadOnly(BasePermission):
    """ Object-level permission to only allow everybody to read an object, but only admins to update it. """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return request.user and type(request.user) is not AnonymousUser and request.user.is_admin


class IsStaffOrReadOnly(BasePermission):
    """ Object-level permission to only allow everybody to read an object, but only staff can update it. """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return request.user and type(request.user) is not AnonymousUser and request.user.is_staff

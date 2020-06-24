from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.throttling import UserRateThrottle


class IsModeratorUser(BasePermission):
    """
    Allows access only to moderators.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='moderators').exists())


class DefaultUserThrottle(UserRateThrottle):
    # check https://stackoverflow.com/questions/34538695/django-rest-framework-per-user-throttles
    rate = '1000/day'


class IsLoggedIn(IsAuthenticated):
    pass


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit it.
    Assumes the model instance has an `created_by` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.created_by == request.user


class IsCreatorOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_moderator = bool(request.user and request.user.groups.filter(name='moderators').exists())
        is_creator = obj.created_by == request.user
        return is_moderator or is_creator


class IsCreatorOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        is_moderator = bool(request.user and request.user.groups.filter(name='moderators').exists())
        is_creator = obj.created_by == request.user
        return is_moderator or is_creator

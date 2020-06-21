from rest_framework.permissions import BasePermission


class IsModeratorUser(BasePermission):
    """
    Allows access only to moderators.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name='moderators').exists())

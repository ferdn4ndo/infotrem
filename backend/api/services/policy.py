from typing import Type

from rest_framework.request import Request

from api.errors.permission_denied_exception import PermissionDeniedException
from api.models import get_object_or_404
from core.models.generic_audited_model import GenericAuditedModel


def ensure_object_owner_or_deny(
        request: Request,
        model_type: Type[GenericAuditedModel],
        pk: str,
        owner_field: str = 'created_by',
):
    instance = get_object_or_404(model_type.objects.all(), pk=pk)

    if not request.user.is_staff and not request.user.is_admin and getattr(instance, owner_field) != request.user:
        raise PermissionDeniedException("You don't have enough permissions to perform the requested operation.")

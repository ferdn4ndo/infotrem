from django.db.models import QuerySet

from api.errors.not_found_exception import NotFoundException
from core.exceptions.model_not_found_exception import ModelNotFoundException
from core.models import get_object_or_error


def get_object_or_404(queryset: QuerySet, error_message: str = None, *args, **kwargs):
    error_message = error_message if error_message is not None else NotFoundException.default_detail
    try:
        return get_object_or_error(queryset=queryset, error_message=error_message, *args, **kwargs)
    except ModelNotFoundException as exc:
        raise NotFoundException(detail=exc.detail)

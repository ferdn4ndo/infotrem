from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class PermissionDeniedException(BaseApiException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = translation.Messages.MSG_NOT_ENOUGH_PERMS
    default_code = 'permission_denied'

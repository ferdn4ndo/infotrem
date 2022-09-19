from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class ConflictException(BaseApiException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = translation.Messages.MSG_CONFLICT
    default_code = 'conflict'

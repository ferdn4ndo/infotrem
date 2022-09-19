from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class InternalServerException(BaseApiException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = translation.Messages.MSG_INTERNAL_ERROR
    default_code = 'internal_server_error'

from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class NotFoundException(BaseApiException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = translation.Messages.MSG_NOT_FOUND
    default_code = 'not_found'

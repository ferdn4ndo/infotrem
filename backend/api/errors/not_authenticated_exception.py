from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class NotAuthenticatedException(BaseApiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = translation.Messages.MSG_NOT_AUTHENTICATED
    default_code = 'not_authenticated'

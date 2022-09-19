from rest_framework import status

from api.errors.base_api_exception import BaseApiException
from api.services import translation


class PreconditionFailedException(BaseApiException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = translation.Messages.MSG_PRECONDITION_FAILED
    default_code = 'precondition_failed'

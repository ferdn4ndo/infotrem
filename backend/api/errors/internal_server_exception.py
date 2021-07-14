from rest_framework import exceptions, status

from api.services import translation


class InternalServerException(exceptions.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = translation.Messages.MSG_INTERNAL_ERROR
    default_code = 'internal_server_error'

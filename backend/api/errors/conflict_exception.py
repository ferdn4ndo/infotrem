from rest_framework import exceptions, status

from api.services import translation


class ConflictException(exceptions.APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = translation.Messages.MSG_CONFLICT
    default_code = 'conflict'

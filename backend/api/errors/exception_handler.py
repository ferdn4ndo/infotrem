import os
import traceback
from typing import Dict

from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import set_rollback

from core.exceptions.authorization_rule_exception import AuthorizationRuleException
from core.exceptions.model_not_found_exception import ModelNotFoundException
from core.services.logger.logger_service import get_logger
from core.services.translation.translation_service import Messages
from .bad_request_exception import BadRequestException
from .base_api_exception import BaseApiException
from .internal_server_exception import InternalServerException
from .not_authenticated_exception import NotAuthenticatedException
from .not_found_exception import NotFoundException
from .permission_denied_exception import PermissionDeniedException


def custom_exception_handler(exception: Exception, context):
    # The context argument is not used by the default handler, but can be useful if the exception handler needs
    # further information such as the view currently being handled, which can be accessed as context['view'].

    if isinstance(exception, Http404):
        exception = NotFoundException()
    elif isinstance(exception, ModelNotFoundException):
        exception = NotFoundException(exception.detail)
    elif isinstance(exception, exceptions.PermissionDenied):
        exception = PermissionDeniedException(exception.detail)
    elif isinstance(exception, AuthorizationRuleException):
        exception = PermissionDeniedException(exception.detail)
    elif isinstance(exception, exceptions.NotAuthenticated):
        exception = NotAuthenticatedException(exception.detail)
    elif isinstance(exception, exceptions.AuthenticationFailed):
        exception = NotAuthenticatedException(exception.detail)
    elif isinstance(exception, exceptions.ValidationError):
        exception = BadRequestException(detail=exception.detail)
    elif isinstance(exception, ValidationError):
        exception = BadRequestException(detail=str(exception))
    else:
        get_logger(__name__).error(exception)
        exception = InternalServerException(detail=str(exception))

    debug = os.getenv("DEBUG", "0") == "1"
    if not debug and isinstance(exception, InternalServerException):
        exception.detail = InternalServerException.default_detail

    return prepare_error_response(exception, context=context, debug=debug)


def prepare_error_response(exception: BaseApiException, context, debug: bool = False) -> Response:
    headers = {}
    if hasattr(exception, 'auth_header'):
        headers['WWW-Authenticate'] = getattr(exception, 'auth_header')
    if hasattr(exception, 'wait'):
        headers['Retry-After'] = '%d' % getattr(exception, 'wait')

    if isinstance(exception.detail, (list, dict)):
        data = {
            'message': Messages.MSG_ONE_OR_MORE_ERRORS_OCCURRED,
            'errors': exception.detail
        }
    else:
        data = {
            'message': exception.detail
        }

    if debug:
        data['debug'] = prepare_debug_information(exception=exception, context=context)

    set_rollback()

    return Response(data, status=exception.status_code, headers=headers)


def prepare_debug_information(exception: BaseApiException, context) -> Dict:
    view = context['view']
    request = context['request']

    debug_info = {
        'exception': str(exception.__class__.__name__),
        'traceback': traceback.format_exc(),
        'view': {
            'class': str(view.__class__.__name__),
            'action': getattr(view, 'action', ''),
            'basename': getattr(view, 'basename', ''),
        },
        'args': context['args'],
        'kwargs': context['kwargs'],
        'user': str(request.user),
        'request': {
            'url': request.build_absolute_uri(),
            'method': request.method,
            'headers': request.headers,
            'data': request.data,
            'query_params': request.query_params,
            'content_type': request.content_type,
        },
    }

    get_logger(__name__).debug(debug_info)

    return debug_info

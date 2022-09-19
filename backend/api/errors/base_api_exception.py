from rest_framework.exceptions import APIException

from core.exceptions.base_core_exception import BaseCoreException


class BaseApiException(BaseCoreException, APIException):
    details: str

    def __init__(self, details: str = ""):
        self.detail = details

    def __str__(self):
        return str(self.details)

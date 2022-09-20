import datetime
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

import api.policies.allow_all_policy
from api.services import throttling


class HealthViewSet(ViewSet):
    permission_classes = [api.policies.allow_all_policy.AllowAllPolicy]
    throttle_classes = (throttling.HealthCheckRateThrottle,)

    def list(self, request: Request):
        """
        Read the health status
        """
        health_response = {
            "datetime": datetime.datetime.utcnow(),
        }

        return Response(health_response, status=status.HTTP_200_OK)

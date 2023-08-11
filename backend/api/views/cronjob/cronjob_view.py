from django.conf import settings
from django_cron import CronJobManager, get_class
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import api.policies.allow_all_policy


class CronJobView(APIView):
    permission_classes = [api.policies.allow_all_policy.AllowAllPolicy]

    def get(self, request, format=None):
        cron_class_names = getattr(settings, 'CRON_CLASSES', [])

        try:
            jobs_to_run = [get_class(x) for x in cron_class_names]
        except Exception:
            return Response('Make sure the cron class names are valid', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        for cron_class in jobs_to_run:
            with CronJobManager(cron_class) as manager:
                manager.run()

        return Response("Crons executed: {}".format(", ".join(cron_class_names)))

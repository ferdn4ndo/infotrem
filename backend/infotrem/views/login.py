from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@method_decorator(csrf_exempt, name='dispatch')
class PerformLogin(View):

    @permission_classes((AllowAny,))
    def post(self, request):
        """
        Token-based authentication
        Adapted from https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb

        :param request:
        :return:
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is None or password is None:
            return JsonResponse({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return JsonResponse({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key}, status=HTTP_200_OK)

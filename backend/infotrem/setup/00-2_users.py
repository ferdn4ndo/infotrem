import os

from django.contrib.auth.models import User


def run():
    try:
        system_user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])
    except User.DoesNotExist:
        system_user = User.objects.create_user(os.environ['SYSTEM_USER_NAME'], password=os.environ['SYSTEM_USER_PASS'])
        system_user.is_superuser = True
        system_user.is_staff = True
        system_user.save()

    try:
        test_user = User.objects.get(username=os.environ['TEST_USER_NAME'])
    except User.DoesNotExist:
        test_user = User.objects.create_user(os.environ['TEST_USER_NAME'], password=os.environ['TEST_USER_PASS'])
        test_user.is_superuser = False
        test_user.is_staff = False
        test_user.save()

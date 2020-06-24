import os

from django.contrib.auth.models import User

try:
    system_user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])
    print("System user already exists!")
except User.DoesNotExist:
    system_user = User.objects.create_user(os.environ['SYSTEM_USER_NAME'], password=os.environ['SYSTEM_USER_PASS'])
    system_user.is_superuser = True
    system_user.is_staff = True
    system_user.save()
    print("System user created!")

try:
    test_user = User.objects.get(username=os.environ['TEST_USER_NAME'])
    print("Test user already exists!")
except User.DoesNotExist:
    test_user = User.objects.create_user(os.environ['TEST_USER_NAME'], password=os.environ['TEST_USER_PASS'])
    test_user.is_superuser = False
    test_user.is_staff = False
    test_user.save()
    print("Test user created!")

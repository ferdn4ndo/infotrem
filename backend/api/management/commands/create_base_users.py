import os

from django.core.management.base import BaseCommand

from api.models.user_model import User


class Command(BaseCommand):
    help = 'Update the list of holidays'
    indexes = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('--verbose', type=bool, default=False, help="Increase text output. Useful for debugging.")

    def handle(self, *args, **options):
        try:
            system_user = User.objects.get(email=os.environ['SYSTEM_USER_NAME'])
            self.stdout.write("System user {} already exists!".format(system_user.email))
        except User.DoesNotExist:
            system_user = User(email=os.environ['SYSTEM_USER_NAME'], password=os.environ['SYSTEM_USER_PASS'])
            system_user.is_superuser = True
            system_user.is_staff = True
            system_user.save()
            self.stdout.write("System user {} created!".format(system_user.email))

        try:
            test_user = User.objects.get(email=os.environ['TEST_USER_NAME'])
            self.stdout.write("Test user {} already exists!".format(test_user.email))
        except User.DoesNotExist:
            test_user = User(email=os.environ['TEST_USER_NAME'], password=os.environ['TEST_USER_PASS'])
            test_user.is_superuser = False
            test_user.is_staff = False
            test_user.save()
            self.stdout.write("Test user {} created!".format(test_user.email))

        self.stdout.write(self.style.SUCCESS('Users {} and {} are present on the database!'.format(
            system_user.email,
            test_user.email,
        )))

from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.models.location_city_model import LocationCity
from api.models.location_state_model import LocationState


class UserManager(BaseUserManager):
    """
    Custom user model manager where uuid is the unique identifiers
    for authentication instead of usernames and tokens are the
    passwords.
    """
    def create_user(self, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not password:
            raise ValueError(_("The password must be set"))
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(_("Superuser must have is_admin=True."))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        return self.create_user(password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    email_validated = models.BooleanField(default=False)
    email_validation_sent = models.BooleanField(default=False)
    email_validation_hash = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.BigIntegerField(null=True)
    birth_date = models.DateField(null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    number = models.PositiveIntegerField(null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(to=LocationCity, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(to=LocationState, null=True, on_delete=models.SET_NULL)
    zipcode = models.PositiveIntegerField(null=True)
    phone = models.BigIntegerField(null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Record creation timestamp"))
    last_activity_at = models.DateTimeField(
        verbose_name=_("Last activity registered by the user in the system"),
        default=timezone.now
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Record last update timestamp"), null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """
        String representation of the model, defined by the UUID
        """
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def is_complete(self) -> bool:
        return (
            self.name is not None
            and self.email is not None
            and self.cpf is not None
            and self.birth_date is not None
            and self.address is not None
            and self.city is not None
            and self.state is not None
            and self.zipcode is not None
        )

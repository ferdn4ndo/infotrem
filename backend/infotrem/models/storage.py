import base64
import os
import random
import shutil
import string
import time
import uuid

from pathlib import Path
from urllib.parse import urlparse

from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from infotrem.errors import MissingLocalTempFile
from infotrem.services.amazon import upload_from_temp, download_to_temp
from infotrem.services.file import get_mime_type, generate_file_hash
from infotrem.services.web import download_url


def generate_random_signature_key() -> str:
    """Generate a random string of letters and digits and special characters """
    password_characters = string.ascii_letters + string.digits
    generated_key = ''.join(random.choice(password_characters) for i in range(32))
    return str(base64.urlsafe_b64encode(generated_key.encode('utf-8')))


class StorageFile(models.Model):

    class Meta:
        app_label = 'infotrem'

    class FileType(models.TextChoices):
        TYPE_IMAGE = 'IMAGE', _('Image')
        TYPE_VIDEO = 'VIDEO', _('Video')

    class StorageType(models.TextChoices):
        STORAGE_S3 = 'AMAZON_S3', _('Amazon S3')
        STORAGE_LOCAL = 'LOCAL', _('Local')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    signature_key = models.CharField(max_length=64, default=generate_random_signature_key)
    file_type = models.CharField(max_length=10, choices=FileType.choices, null=True)
    file_size = models.PositiveIntegerField(verbose_name="File size in bytes")
    file_hash = models.CharField(max_length=64, null=True, verbose_name="SHA256 hash of the processed file")
    mime_type = models.CharField(max_length=255)
    original_filename = models.CharField(max_length=255)
    large_file_path = models.CharField(max_length=1024, null=True)
    small_file_path = models.CharField(max_length=1024, null=True)
    storage_file_path = models.CharField(max_length=1024, null=True)
    storage_type = models.CharField(max_length=10, choices=StorageType.choices, default=StorageType.STORAGE_S3)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)

    def __str__(self):
        return self.storage_file_path

    def set_type_from_mime(self):
        """
        ToDo
        :return:
        """
        mime_to_type_dict = {
            'image/jpeg': self.FileType.TYPE_IMAGE,
            'image/png': self.FileType.TYPE_IMAGE,
            'image/tiff': self.FileType.TYPE_IMAGE,
            'image/bmp': self.FileType.TYPE_IMAGE,
            'image/gif': self.FileType.TYPE_IMAGE,
            'video/mp4': self.FileType.TYPE_VIDEO,
            'video/3gpp': self.FileType.TYPE_VIDEO,
        }
        self.file_type = mime_to_type_dict[self.mime_type] if self.mime_type in mime_to_type_dict else None

    def get_signature(self):
        """
        ToDo
        :return:
        """
        text = '#INFOTREM#{}#{}#{}#'.format(self.id, self.created_by.username, time.time())
        fernet_cryptor = Fernet(self.signature_key)
        return fernet_cryptor.encrypt(bytes(text))

    def get_temp_file_path(self):
        """
        ToDo
        :return:
        """
        temp_dir = os.environ['TEMP_PATH'] or '/temp'
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        return os.path.join(temp_dir, str(self.id))

    def get_storage_file_path(self):
        """
        ToDo
        :return:
        """
        if self.storage_file_path is not None:
            return self.storage_file_path
        return "{}/{}".format(os.environ['AWS_S3_FOLDER'], str(self.id))

    def pull_to_temp(self):
        """
        ToDo
        :return:
        """
        temp_path = download_to_temp(remote_path=self.get_storage_file_path(), temp_path=self.get_temp_file_path())

    def push_from_temp(self):
        """
        ToDo
        :return:
        """
        temp_path = self.get_temp_file_path()
        if not os.path.isfile(temp_path):
            raise MissingLocalTempFile(
                "Either generate the file at {} manually or call the pull_to_temp method".format(temp_path)
            )

        upload_from_temp(temp_path, self.get_storage_file_path())

        self.storage_file_path = self.get_storage_file_path()
        self.save()

    @staticmethod
    def create_from_temp_fle(temp_file_path: str, original_filename: str, user: User):
        mime = get_mime_type(temp_file_path)

        storage_file = StorageFile(
            file_type=StorageFile.FileType.TYPE_IMAGE,
            file_size=Path(temp_file_path).stat().st_size,
            file_hash=generate_file_hash(temp_file_path),
            original_filename=original_filename,
            mime_type=mime,
            created_by=user,
        )
        storage_file.set_type_from_mime()

        storage_local_path = storage_file.get_temp_file_path()
        shutil.move(temp_file_path, storage_local_path)

        storage_file.push_from_temp()

        return storage_file

    @staticmethod
    def create_from_url(url: str, user: User):
        parser = urlparse(url)
        original_filename = os.path.basename(parser.path)

        temp_file_path = download_url(url)

        return StorageFile.create_from_temp_fle(
            temp_file_path=temp_file_path,
            original_filename=original_filename,
            user=user
        )

import uuid
from typing import Union

from django.contrib.auth.models import User
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from django.db import models
from django.utils import timezone

from infotrem.errors import InvalidArgumentClass, InvalidFileMimeType, UnreachableURL
from infotrem.models.location_model import Location
from infotrem.models.railroad_company_model import RailroadCompanyPaintScheme
from infotrem.models.rolling_stock import RollingStock
from infotrem.models.storage import StorageFile
from infotrem.services.file import save_from_memory, check_if_media
from infotrem.services.photo import \
    get_image_information, \
    get_exif_focal_length, \
    get_exif_aperture, \
    get_exif_flash_fired, \
    get_exif_orientation, \
    get_exif_exposition
from infotrem.services.web import check_if_url_is_downloadable, download_url, get_file_name_from_url


class MediaItem(models.Model):

    class Meta:
        app_label = 'infotrem'

    class MediaStatus(models.TextChoices):
        DRAFT = 'Draft (not ready for processing yet)'
        QUEUE = 'In the queue (waiting for processing)'
        PROCESSING = 'Being processed by a worker'
        REVIEW = 'Media is waiting approval/reject by a moderator'
        PUBLISHED = 'Media was processed, approved and published'
        REJECTED_TEMP = 'Media was temporary rejected, with a possible re-review'
        REJECTED_PERM = 'Media was permanently rejected'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=65535, null=True)
    file_raw = models.ForeignKey(to=StorageFile, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=MediaStatus.choices, default=MediaStatus.DRAFT)
    raw_height = models.PositiveIntegerField(verbose_name="Height of the raw media item", null=True)
    raw_width = models.PositiveIntegerField(verbose_name="Width of the raw media item", null=True)
    location = models.ForeignKey(to=Location, on_delete=models.SET_NULL, null=True)
    known_author = models.BooleanField(default=False, verbose_name="If the author is known")
    author_confirmed = models.BooleanField(default=False, verbose_name="If the author is in the system and confirmed")
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="media_author+")
    original_url = models.TextField(max_length=255, null=True, verbose_name="Original URL, if downloaded")
    references = models.TextField(max_length=1024, null=True)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)

    @staticmethod
    def create_from_storage_file(storage_file: StorageFile):
        media_item = MediaItem(file_raw=storage_file)

        if storage_file.file_type == StorageFile.FileType.TYPE_IMAGE:
            media_item.update_image_media_item()

        return media_item

    @staticmethod
    def create_from_request_file(request_file: Union[TemporaryUploadedFile, InMemoryUploadedFile], user: User):
        if isinstance(request_file, TemporaryUploadedFile):
            temp_file_path = request_file.temporary_file_path()
        elif isinstance(request_file, InMemoryUploadedFile):
            temp_file_path = save_from_memory(request_file)
        else:
            raise InvalidArgumentClass

        if not check_if_media(temp_file_path):
            raise InvalidFileMimeType

        original_filename = request_file.name
        storage_file = StorageFile.create_from_temp_fle(temp_file_path, original_filename, user)
        media_item = MediaItem.create_from_storage_file(storage_file)

        return media_item

    @staticmethod
    def create_from_url(url: str, user: User):
        if not check_if_url_is_downloadable(url):
            raise UnreachableURL("Did not received a 200 status from {}".format(url))

        temp_file_path = download_url(url)

        if not check_if_media(temp_file_path):
            raise InvalidFileMimeType

        original_filename = get_file_name_from_url(url)
        storage_file = StorageFile.create_from_temp_fle(temp_file_path, original_filename, user)

        media_item = MediaItem.create_from_storage_file(storage_file)
        media_item.original_url = url
        media_item.save()

        return media_item

    def update_image_media_item(self):
        if self.file_raw is None:
            return

        data = get_image_information(self.file_raw.get_temp_file_path())
        self.raw_height = data['IMAGE_HEIGHT']
        self.raw_width = data['IMAGE_WIDTH']
        self.save()

        orientation_dict = get_exif_orientation(data)

        image_item = ImageMediaItem.objects.filter(media_item=self)

        if len(image_item) == 0:
            image_item = ImageMediaItem(media_item=self)
            image_item.save()

        image_item.focal_length = get_exif_focal_length(data)
        image_item.aperture = get_exif_aperture(data)
        image_item.iso = data['ISOSpeedRatings'] if 'ISOSpeedRatings' in data else None
        image_item.flash_fired = get_exif_flash_fired(data)
        image_item.orientation_angle = orientation_dict['orientation_angle'] if orientation_dict is not None else None
        image_item.is_flipped = orientation_dict['is_flipped'] if orientation_dict is not None else None
        image_item.exposition = get_exif_exposition(data)
        image_item.datetime_taken = data['DateTimeOriginal'] if 'DateTimeOriginal' in data else None
        image_item.camera_manufacturer = data['Make'] if 'Make' in data else None
        image_item.camera_model = data['Model'] if 'Model' in data else None
        image_item.exif_image_height = data['ExifImageHeight'] if 'ExifImageHeight' in data else None
        image_item.exif_image_width = data['ExifImageWidth'] if 'ExifImageWidth' in data else None

        image_item.save()


class ImageMediaItem(models.Model):

    class Meta:
        app_label = 'infotrem'

    media_item = models.OneToOneField(to=MediaItem, on_delete=models.CASCADE, primary_key=True, editable=False)
    focal_length = models.FloatField(null=True, verbose_name="Focal length of the lenses in millimeters")
    aperture = models.CharField(max_length=255, null=True)
    flash_fired = models.BooleanField(null=True)
    iso = models.PositiveIntegerField(null=True)
    orientation_angle = models.IntegerField(null=True)
    is_flipped = models.BooleanField(null=True)
    exposition = models.CharField(max_length=255, null=True)
    datetime_taken = models.CharField(max_length=255, null=True)
    camera_manufacturer = models.CharField(max_length=255, null=True)
    camera_model = models.CharField(max_length=255, null=True)
    exif_image_height = models.IntegerField(null=True)
    exif_image_width = models.IntegerField(null=True)


class ImageMediaItemSize(models.Model):

    class Meta:
        app_label = 'infotrem'

    class SizeTag(models.TextChoices):
        """ Height = math.ceil((Width*2/3)/32)*32 """
        SIZE_8K = '8K (máx 8192x5472 px @ 3:2, 45 Megapixels)'  # ~8K UHD
        SIZE_4K = '4K (máx 4096x2752 px @ 3:2, 11 Megapixels)'  # ~DCI 4K
        SIZE_3K = '3K (máx 3200x2144 px @ 3:2, 6.9 Megapixels)'  # ~QHD+
        SIZE_2K = '2K (máx 2048x1376 px @ 3:2, 2.8 Megapixels)'  # ~DCI 2K
        SIZE_1K = '1K (máx 1280x864 px @ 3:2, 1.1 Megapixels)'  # ~HD
        SIZE_THUMB_LARGE = 'Large Thumbnail (960×640 px)'  # DVGA
        SIZE_THUMB_MEDIUM = 'Medium Thumbnail (480×320 px)'  # WQVGA
        SIZE_THUMB_SMALL = 'Small Thumbnail (240x160 px)'  # HQVGA

    media_item = models.OneToOneField(to=MediaItem, on_delete=models.CASCADE, primary_key=True, editable=False)
    file_raw = models.ForeignKey(to=StorageFile, on_delete=models.CASCADE)
    size_tag = models.CharField(max_length=10, choices=SizeTag.choices, null=True)
    raw_height = models.PositiveIntegerField(verbose_name="Height of the sized media item", null=True)
    raw_width = models.PositiveIntegerField(verbose_name="Width of the sized media item", null=True)


class MediaItemReview(models.Model):

    class Meta:
        app_label = 'infotrem'

    class ReviewDecision(models.TextChoices):
        REQUEST_CHANGES = "Request changes (media will be temporary rejected until the author uploads it again)"
        APPROVED = "Approved with no changes needed"
        REJECTED = "Reject without possibility of updating the image"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media_item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE)
    moderator = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    decision = models.CharField(max_length=10, choices=ReviewDecision.choices, null=True)
    comment = models.CharField(max_length=1024, null=True)
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="editor+")


class MediaItemRollingStock(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media_item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE)
    rolling_stock = models.ForeignKey(to=RollingStock, on_delete=models.CASCADE)
    paint_scheme = models.ForeignKey(to=RailroadCompanyPaintScheme, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)


class MediaItemLike(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE, editable=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)


class MediaItemFavorite(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE, editable=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)


class MediaItemComment(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE, editable=False)
    replies_to = models.ForeignKey('self', null=True, verbose_name='Replies to', on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)


class MediaAlbum(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=65535)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)


class MediaAlbumItem(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    album = models.ForeignKey(to=MediaAlbum, on_delete=models.CASCADE, editable=False)
    item = models.ForeignKey(to=MediaItem, on_delete=models.CASCADE, editable=False)
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name="Record last update timestamp", null=True)


class MediaAlbumLike(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    album = models.ForeignKey(to=MediaAlbum, on_delete=models.CASCADE, editable=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)


class MediaAlbumFavorite(models.Model):

    class Meta:
        app_label = 'infotrem'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    album = models.ForeignKey(to=MediaAlbum, on_delete=models.CASCADE, editable=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creator+")
    created_at = models.DateTimeField(verbose_name="Record creation timestamp", default=timezone.now, editable=False)

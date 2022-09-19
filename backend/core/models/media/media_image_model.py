from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.generic_audited_model import GenericAuditedModel
from core.models.media.media_model import Media
from core.services.photo.photo_exif_service import PhotoExifService


class MediaImage(GenericAuditedModel):

    media = models.OneToOneField(to=Media, on_delete=models.CASCADE, editable=False)
    focal_length = models.FloatField(null=True, verbose_name=_("Focal length of the lenses in millimeters"))
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
    size_tag = models.CharField(
        max_length=64,
        null=True,
        choices=Media.MediaSizeTag.choices,
        verbose_name=_("Biggest size tag of the media item")
    )
    raw_height = models.PositiveIntegerField(verbose_name="Height of the raw media item", null=True)
    raw_width = models.PositiveIntegerField(verbose_name="Width of the raw media item", null=True)

    def update_data_from_path(self, file_path: str):

        service = PhotoExifService(file_path=file_path)
        data = service.get_image_information()
        orientation_dict = service.get_exif_orientation()

        self.focal_length = service.get_exif_focal_length()
        self.aperture = service.get_exif_aperture()
        self.iso = data['ISOSpeedRatings'] if 'ISOSpeedRatings' in data else None
        self.flash_fired = service.get_exif_flash_fired()
        self.orientation_angle = orientation_dict['orientation_angle'] if orientation_dict is not None else None
        self.is_flipped = orientation_dict['is_flipped'] if orientation_dict is not None else None
        self.exposition = service.get_exif_exposition()
        self.datetime_taken = data['DateTimeOriginal'] if 'DateTimeOriginal' in data else None
        self.camera_manufacturer = data['Make'] if 'Make' in data else None
        self.camera_model = data['Model'] if 'Model' in data else None
        self.exif_image_height = data['ExifImageHeight'] if 'ExifImageHeight' in data else None
        self.exif_image_width = data['ExifImageWidth'] if 'ExifImageWidth' in data else None

        self.save()


class MediaImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaImage, MediaImageAdmin)

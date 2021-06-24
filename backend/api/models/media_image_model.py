from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel
from api.models.media_model import Media
from api.services.photo import get_image_information,\
    get_exif_orientation,\
    get_exif_focal_length,\
    get_exif_aperture, \
    get_exif_flash_fired,\
    get_exif_exposition


class MediaImage(GenericAuditedModel):

    media_item = models.OneToOneField(to=Media, on_delete=models.CASCADE, editable=False)
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

    def update_data_from_path(self, file_path: str):
        data = get_image_information(file_path)
        orientation_dict = get_exif_orientation(data)

        self.focal_length = get_exif_focal_length(data)
        self.aperture = get_exif_aperture(data)
        self.iso = data['ISOSpeedRatings'] if 'ISOSpeedRatings' in data else None
        self.flash_fired = get_exif_flash_fired(data)
        self.orientation_angle = orientation_dict['orientation_angle'] if orientation_dict is not None else None
        self.is_flipped = orientation_dict['is_flipped'] if orientation_dict is not None else None
        self.exposition = get_exif_exposition(data)
        self.datetime_taken = data['DateTimeOriginal'] if 'DateTimeOriginal' in data else None
        self.camera_manufacturer = data['Make'] if 'Make' in data else None
        self.camera_model = data['Model'] if 'Model' in data else None
        self.exif_image_height = data['ExifImageHeight'] if 'ExifImageHeight' in data else None
        self.exif_image_width = data['ExifImageWidth'] if 'ExifImageWidth' in data else None

        self.save()


class MediaImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaImage, MediaImageAdmin)

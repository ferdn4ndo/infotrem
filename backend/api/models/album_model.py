from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.models.generic_audited_model import GenericAuditedModel


class Album(GenericAuditedModel):

    title = models.CharField(max_length=255, verbose_name=_("Title of the album"))
    description = models.TextField(max_length=65535, verbose_name=_("Description of the album"))


class AlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)

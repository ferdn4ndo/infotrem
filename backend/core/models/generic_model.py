import uuid
from typing import Dict

from django.utils.translation import gettext_lazy as _
from django.db import models


class GenericModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("Record primary key (UUID v4)")
    )

    class Meta:
        abstract = True

    def __str__(self):
        return '%s object (%s)' % (self.__class__.__name__, self.id)

    def update_from_dict(self, input_data: Dict):
        for attribute, value in input_data.items():
            if not hasattr(self, attribute):
                f"The attribute '{attribute}' wasn't found in the {self.__class__.__name__} model."

            setattr(self, attribute, value)

    objects = models.Manager()

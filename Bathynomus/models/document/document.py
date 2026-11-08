"""Module providing Document tables for Bathynomus"""

import uuid

from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.utils.private_media import FileStorage


class Document(CommonInfo):
    """Class containing Document fields."""

    key = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    description = models.CharField(max_length=255)
    url_location = models.TextField(
        # Contains URLS
        blank=True,
        default="",
    )
    document = models.FileField(blank=True, null=True, storage=FileStorage())
    upload_successfully = models.BooleanField(
        default=False,
    )
    is_purged = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return str(self.description)

    class Meta:
        """Meta definition for Document model."""

        verbose_name_plural = "Documents"

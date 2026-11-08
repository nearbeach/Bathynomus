from django.db import models
import uuid

from Bathynomus.models.abstraction.common_abstractions import CommonInfo


class Folder(CommonInfo):
    """Class containing fields for the Folder model."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    folder_name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

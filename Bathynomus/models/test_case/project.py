from django.db import models
from Bathynomus.models.abstraction.common_abstractions import CommonInfo
import uuid


class Project(CommonInfo):
    """Class containing fields for the Project model."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        default="",
    )

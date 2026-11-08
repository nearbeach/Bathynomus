from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.product import Product
import uuid


class TestRun(CommonInfo):
    """Class containing fields for Test Runs."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    project_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        default="",
    )
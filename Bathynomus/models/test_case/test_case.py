"""Module providing Test Cases tables for Bathynomus."""
from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.product import Product
import uuid


class TestCase(CommonInfo):
    """Class containing fields for Test Cases."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    project_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    folder_id = models.ForeignKey(
        "Folder",
        on_delete=models.CASCADE,
    )
    current_version_id = models.ForeignKey(
        "TestCaseVersion",
        on_delete=models.CASCADE,
        null=True,
    )

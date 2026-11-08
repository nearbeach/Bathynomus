from django.db import models
import uuid

from Bathynomus.models.abstraction.common_abstractions import CommonInfo


class TestCaseStep(CommonInfo):
    """Class containing fields for Test Case Steps."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    version_id = models.ForeignKey(
        "TestCaseVersion",
        on_delete=models.CASCADE,
    )
    step_order = models.IntegerField()
    action = models.TextField(
        blank=True,
        default="",
    )
    expected_result = models.TextField(
        blank=True,
        default="",
    )

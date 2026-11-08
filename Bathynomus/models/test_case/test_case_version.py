from django.db import models
import uuid

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.utils.enums.automation_enum import AutomationStatus
from Bathynomus.utils.enums.priority_enum import ObjectPriority


class TestCaseVersion(CommonInfo):
    """Class containing fields for Test Case Versions."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    test_case_id = models.ForeignKey(
        "TestCase",
        on_delete=models.CASCADE,
    )
    version_number = models.BigIntegerField(
        blank=False,
        null=False,
    )
    title = models.CharField(max_length=255)
    preconditions = models.TextField(
        blank=True,
        default="",
    )
    priority = models.IntegerField(
        choices=ObjectPriority,
        default=ObjectPriority.NORMAL,
    )
    automation_status = models.IntegerField(
        choices=AutomationStatus,
        default=AutomationStatus.MANUAL,
    )
    change_note = models.TextField(
        blank=True,
        default="",
    )

    class Meta:
        """Meta-information for TestCaseVersion model"""
        unique_together = ("test_case_id", "version_number")

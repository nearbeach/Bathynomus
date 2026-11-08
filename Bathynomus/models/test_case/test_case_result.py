from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.utils.enums.status_enum import TestRunStatus

import uuid


class TestCaseResult(CommonInfo):
    """Class containing fields for Test Case Results."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    run_id = models.ForeignKey(
        "TestRun",
        on_delete=models.CASCADE,
    )
    test_case_version_id = models.ForeignKey(
        "TestCaseVersion",
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(
        choices=TestRunStatus,
        default=TestRunStatus.NOT_RUN,
    )
    notes = models.TextField(
        blank=True,
        default="",
    )
    executed_by = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    executed_at = models.DateTimeField(
        auto_now_add=True,
    )

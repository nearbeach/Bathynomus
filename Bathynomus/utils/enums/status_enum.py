from django.db import models
from django.utils.translation import gettext_lazy as _


class TestRunStatus(models.IntegerChoices):
    """Class of enum options for Test Run Status"""

    NOT_RUN = 0, _("Not Run")
    IN_PROGRESS = 1, _("In Progress")
    PASSED = 2, _("Passed")
    FAILED = 3, _("Failed")
    BLOCKED = 4, _("Blocked")
    SKIPPED = 5, _("Skipped")

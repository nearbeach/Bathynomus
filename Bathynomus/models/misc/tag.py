"""Module provides Tag tables for NearBeach"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from Bathynomus.models.abstraction.common_abstractions import CommonInfo


class Tag(CommonInfo):
    """Class contains fields for Tag table"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=50,
    )
    colour = models.CharField(
        max_length=7,
        default="#651794",
    )
    text_colour = models.CharField(
        max_length=7,
        default="#ffffff",
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        """Meta-definition for Tag table."""

        verbose_name_plural = "Tags"


class TagAssignment(CommonInfo):
    """Class contains fields for the Tag Assignment table"""

    class ObjectEnum(models.TextChoices):
        """Class contains enum choices for object enum."""

        PROJECT = "project", _("Project")
        REQUIREMENT = "requirement", _("Requirement")
        TEST_CASE = "test_case", _("Test Case")
        TEST_RUN = "test_run", _("Test Run")

    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )
    object_enum = models.CharField(
        max_length=40,
        choices=ObjectEnum,
        default=ObjectEnum.REQUIREMENT,
    )
    object_id = models.IntegerField(
        default=0,
    )

    class Meta:
        """Meta-definition for TagAssignment table."""

        verbose_name_plural = "Tag Assignments"

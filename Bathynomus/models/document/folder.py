"""Module providing Folder tables for Bathynomus"""

from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.customer import CustomerForeignKey
from Bathynomus.models.kanban_board.kanban_card import KanbanCardForeignKey
from Bathynomus.models.organisation import OrganisationForeignKey
from Bathynomus.models.project import ProjectForeignKey
from Bathynomus.models.request_for_change.request_for_change import RequestForChangeForeignKey
from Bathynomus.models.requirement.requirement import RequirementForeignKey
from Bathynomus.models.requirement.requirement_item import RequirementItemForeignKey
from Bathynomus.models.task import TaskForeignKey


class Folder(
    CommonInfo,
    ProjectForeignKey,
    TaskForeignKey,
    CustomerForeignKey,
    OrganisationForeignKey,
    RequirementForeignKey,
    RequirementItemForeignKey,
    RequestForChangeForeignKey,
    KanbanCardForeignKey,
):
    """Class containing Folder fields"""

    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    parent_folder = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return str(self.description)

    class Meta:
        """Meta definition for Folder model."""

        verbose_name_plural = "Folders"

"""Module providing Document tables for Bathynomus"""

from django.db import models
from django.conf import settings

from Bathynomus.models.customer import CustomerForeignKey
from Bathynomus.models.document.document import Document
from Bathynomus.models.document.folder import Folder
from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.kanban_board.kanban_card import KanbanCardForeignKey
from Bathynomus.models.organisation import OrganisationForeignKey
from Bathynomus.models.project import ProjectForeignKey
from Bathynomus.models.request_for_change.request_for_change import RequestForChangeForeignKey
from Bathynomus.models.requirement.requirement import RequirementForeignKey
from Bathynomus.models.requirement.requirement_item import RequirementItemForeignKey
from Bathynomus.models.task import TaskForeignKey


class DocumentPermission(
    CommonInfo,
    CustomerForeignKey,
    KanbanCardForeignKey,
    ProjectForeignKey,
    OrganisationForeignKey,
    RequestForChangeForeignKey,
    RequirementForeignKey,
    RequirementItemForeignKey,
    TaskForeignKey,
):
    """Class containing Document Permission fields"""

    id = models.BigAutoField(primary_key=True)
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    new_object = models.UUIDField(
        blank=True,
        null=True,
    )
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    is_profile_picture = models.BooleanField(
        default=False,
    )
    is_purged = models.BooleanField(
        default=False,
    )

    class Meta:
        """Meta definition for Document Permission model."""

        verbose_name_plural = "Document Permissions"

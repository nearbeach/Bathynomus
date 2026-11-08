"""Module provides User tables for Bathynomus"""

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.document.document import Document
from Bathynomus.models.permission.group import Group
from Bathynomus.models.permission.permission_set import PermissionSet


class UserGroup(CommonInfo):
    """Class contains fields for the User Group table"""

    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    permission_set = models.ForeignKey(
        PermissionSet,
        on_delete=models.CASCADE,
    )
    report_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="report_to",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    group_leader = models.BooleanField(
        default=False,
    )

    class Meta:
        """Meta-definition for UserGroup."""

        verbose_name_plural = "User Groups"
        indexes = [
            models.Index(
                fields=["username", "is_deleted", "group"],
                name="ug_user_deleted_group_idx",
            ),
        ]


class UserProfilePicture(CommonInfo):
    """Class contains fields for the User Profile Picture table"""

    username = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        # Return the document key
        # TODO - key is a UUID, so str() on this model raises TypeError. Should be str(self.document.key)
        return self.document.key  # type: ignore[return-value]

    class Meta:
        """Meta-definition for UserProfilePicture."""

        verbose_name_plural = "User Profile Pictures"


class UserSetting(CommonInfo):
    """Class contains fields for the User Setting table"""

    class SettingType(models.TextChoices):
        """Class containing the setting types for User Settings."""

        DASHBOARD = "DASHBOARD", _("Dashboard")
        EDIT_KANBAN_BOARD = "EDIT_KANBAN_BOARD", _("Edit Kanban Board")
        SEARCH = "SEARCH", _("Search")
        THEME = "THEME", _("Bathynomus Theme")

    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    setting_type = models.CharField(
        max_length=30,
        choices=SettingType,
        default=SettingType.THEME,
    )
    setting_data = models.JSONField()

    class Meta:
        """Meta-definition for UserSetting."""

        verbose_name_plural = "User Settings"

"""Model providing Permission Set tables for NearBeach."""

from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.utils.enums.permission_enum import PermissionLevel, PermissionBoolean


class PermissionSet(CommonInfo):
    """Class containing fields for Permission set table"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
    )
    # ADMINISTRATION PERMISSIONS
    administration_assign_user_to_group = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    administration_create_group = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    administration_create_permission_set = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    administration_create_user = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    # REGULAR PERMISSIONS
    project = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    test_case = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    test_run = models.IntegerField(
        choices=PermissionLevel,
        default=0,
    )
    """
    ADDITIVE permission
    ~~~~~~~~~~~~~~~~~~~~
    Designed to add on extra abilities to those user who have "READ ONLY" for certain modules.
    If a user has the ability to "EDIT" for any of these modules, then this section does not
    need to be populated with data.
    """
    document = models.IntegerField(
        choices=PermissionBoolean,
        default=0,
    )
    test_run_note = models.IntegerField(
        choices=PermissionBoolean,
        default=0,
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        """Meta-definition for a permission set."""

        verbose_name_plural = "Permission Sets"
        ordering = ["name"]

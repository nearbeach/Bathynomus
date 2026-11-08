"""Module providing object assignment tables for Bathynomus."""

from django.db import models
from django.conf import settings

from Bathynomus.models.abstraction.common_abstractions import CommonInfo
from Bathynomus.models.permission.group import Group
from Bathynomus.models.product import Product
from Bathynomus.models.test_case.test_case import TestCase
from Bathynomus.models.test_run.test_run import TestRun

class ObjectAssignment(CommonInfo):
    """
    Class containing fields for the Object Assignment table.

    Object permissions are the centralized permissions for all objects
    - Product
    - Test Case
    - Test Run

    These permissions are only "ACCESS" permissions.
    The user/group's over-riding permissions determine if
    the user can add, edit etc.
    """

    id = models.BigAutoField(primary_key=True)
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_assigned_user",
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    test_case = models.ForeignKey(
        TestCase,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    test_run = models.ForeignKey(
        TestRun,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        """Meta-definitions for the object assignment table"""

        verbose_name_plural = "Object Assignment Tables"

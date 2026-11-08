"""Module providing group tables for Bathynomus"""

from typing import Tuple

from django.db import models

from Bathynomus.models.abstraction.common_abstractions import CommonInfo


class Group(CommonInfo):
    """Class containing fields for group table"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=50,
    )
    parent_group = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def natural_key(self) -> Tuple[int, str]:
        """Method returns a natural key for groups"""
        return self.id, self.name

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        """Meta-definitions for Group"""

        verbose_name_plural = "Groups"

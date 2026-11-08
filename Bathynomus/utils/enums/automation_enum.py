"""Module providing automation enums for Bathynomus."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class AutomationStatus(models.IntegerChoices):
    """Class containing enums for Permission Level"""

    AUTOMATIC = 0, _("Automatic")
    MANUAL = 1, _("Manual")

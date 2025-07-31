from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _
import datetime

class Route(models.Model):
    RouteId = models.AutoField(primary_key=True)
    RouteLocationXAxis = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    RouteLocationYAxis = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    class RouteColourClass(models.TextChoices):
        IRNBRU = "IrnBru", _("Irn-Bru")
        FLAMINGO = "Flamingo", _("Flamingo")
        WASP = "Wasp", _("Wasp")
        MINT = "Mint", _("Mint")
        GREEN = "Green", _("Green")
        ORANGE = "Orange", _("Orange")
        PURPLE = "Purple", _("Purple")
        RED = "Red", _("Red")
        GRYFFINDOR = "Gryffindor", _("Gryffindor")
        PINK = "Pink", _("Pink")
        WHITE = "White", _("White")
        BLACK = "Black", _("Black")
        BLUE = "Blue", _("Blue")
        YELLOW = "Yellow", _("Yellow")
        GREY = "Grey", _("Grey")
        DALMATIANS = "Dalmatians", _("Dalmatians")
        BLOBS = "Blobs", _("Blobs")
    RouteColour = models.CharField(
        max_length=50,
        choices=RouteColourClass.choices,
        default=RouteColourClass.IRNBRU
    )
    class RouteGradeRangeClass(models.TextChoices):
        VB = "VB", _("VB")
        V0V2 = "V0_V2", _("V0-V2")
        V1V3 = "V1_V3", _("V1-V3")
        V2V4 = "V2_V4", _("V2-V4")
        V3V5 = "V3_V5", _("V3-V5")
        V4V6 = "V4_V6", _("V4-V6")
        V5V7 = "V5_V7", _("V5-V7")
        V7PLUS = "V7plus", _("V7+")
        OFFCIRCUIT = "OffCircuit", _("Off Circuit")
        COMP = "Comp", _("Comp")
    RouteGradeRange = models.CharField(
        max_length=50,
        choices=RouteGradeRangeClass.choices,
        default=RouteGradeRangeClass.VB
    )
    RouteCreatedAt = models.DateField(default=datetime.date.today)
    RoutesClimbedByUsers = models.ManyToManyField(User)

    # I was going to have a RouteDestroyedAt date field, but once a route is down,
    # it never goes back up and never can, there really is not a point
    # to storing that information. Might as well try to use db space well

    def __str__(self):
        return 'Route_' + str(self.RouteId)

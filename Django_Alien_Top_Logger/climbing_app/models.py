from django.db import models
from django.utils.translation import gettext_lazy as _

class Route(models.Model):
    RouteId = models.AutoField(primary_key=True)
    RouteLocationXAxis = models.PositiveIntegerField()
    RouteLocationYAxis = models.PositiveIntegerField()
    class RouteColourClass(models.TextChoices):
        RED = "RED", _("RED")
        BLUE = "BLUE", _("BLUE")
        GREEN = "GREEN", _("GREEN")
    RouteColour = models.CharField(
        max_length=50,
        choices=RouteColourClass.choices,
        default=RouteColourClass.RED
    )
    class RouteGradeRangeClass(models.TextChoices):
        V0V2 = "V0-V2", _("V0-V2")
        V1V3 = "V1-V3", _("V1-V3")
        V2V4 = "V2-V4", _("V2-V4")
    RouteGradeRange = models.CharField(
        max_length=50,
        choices=RouteGradeRangeClass.choices,
        default=RouteGradeRangeClass.V0V2
    )
    RouteCreatedAt = models.DateField()
    RouteDestroyedAt = models.DateField()

class ClimbingUser(models.Model):
    ClimbingUserId = models.AutoField(primary_key=True)
    ClimbingUserName = models.CharField(max_length=50)
    ClimbingUserPassword = models.CharField(max_length=50)
    ClimbingUserCreatedAt= models.DateTimeField(auto_now_add=True)
    RoutesClimbedByUser = models.ManyToManyField(Route, through='ClimbingUserRoute')

    def __str__(self):
        return self.ClimbingUserName

class ClimbingUserRoute(models.Model):
    ClimbingUserId = models.ForeignKey(ClimbingUser, on_delete=models.CASCADE)
    RouteId = models.ForeignKey(Route, on_delete=models.CASCADE)
    DateSent = models.DateField()

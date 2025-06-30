from django.db import models
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, AnonymousUser
from django.utils.translation import gettext_lazy as _
import datetime

# class isClimbingStaffMember(Group):
#     name = "isClimbingStaffMember",
#     permissions = ['can_add_route', 'can_delete_route'],
#     class Meta:
#         content_type = ContentType.objects.get_for_model(User)
#         permission = Permission.objects.create(
#             codename="can_add_route",
#             name="Can add routes",
#             content_type=content_type,
#         )
#         permission = Permission.objects.create(
#             codename="can_delete_route",
#             name="Can delete routes",
#             content_type=content_type,
#         )

# class isClimbingCustomer(Group):
#     name = "isClimbingCustomer",
#     permissions = ['can_track_route'],
#     class Meta:
#         content_type = ContentType.objects.get_for_model(User)
#         permission = Permission.objects.create(
#             codename="can_track_their_routes",
#             name="Can track routes that they have climbed",
#             content_type=content_type,
#         )
#         permission = Permission.objects.create(
#             codename="can_see_their_tracked_routes",
#             name="Can see the tracked routes that they have climbed",
#             content_type=content_type,
#         )

class Route(models.Model):
    RouteId = models.AutoField(primary_key=True)
    RouteLocationXAxis = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    RouteLocationYAxis = models.DecimalField(decimal_places=2, max_digits=4, default=0)
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
    RouteCreatedAt = models.DateField(default=datetime.date.today)
    RoutesClimbedByUsers = models.ManyToManyField(User)

    class Meta:
        permissions = [
            ("can_delete_route", "Can delete route"),
            ("can_add_route", "Can add route"),
        ]

    # I was going to have a RouteDestroyedAt datefiles, but once a route is down,
    # it never goes back up and never can, there really is not a point
    # to storing that information. Might as well try to use db space well

    def __str__(self):
        return 'Route_' + str(self.RouteId)


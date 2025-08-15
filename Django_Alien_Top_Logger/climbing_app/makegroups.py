# RUN THIS WHOLE THING IN SHELL AFTER MIGRATIONS HAVE BEEN RUN
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Route

isClimbingStaffMember, created = Group.objects.get_or_create(name='isClimbingStaffMember')
isClimbingCustomer, created = Group.objects.get_or_create(name='isClimbingCustomer')

RouteContentType = ContentType.objects.get_for_model(Route)

can_delete_routes_permission, created = Permission.objects.get_or_create(
    codename='can_delete_routes',
    name='Can delete routes',
    content_type=RouteContentType
)

can_add_routes_permission, created = Permission.objects.get_or_create(
    codename='can_add_routes',
    name='Can add routes',
    content_type=RouteContentType
)

can_track_routes_permission, created = Permission.objects.get_or_create(
    codename='can_track_routes',
    name='Can track routes',
    content_type=RouteContentType
)

isClimbingStaffMember.permissions.add(can_delete_routes_permission)
isClimbingStaffMember.permissions.add(can_add_routes_permission)
isClimbingCustomer.permissions.add(can_track_routes_permission)

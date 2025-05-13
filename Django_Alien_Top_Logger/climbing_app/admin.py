from django.contrib import admin
from .models import ClimbingUser, Route, ClimbingUserRoute

admin.site.register(ClimbingUser)
admin.site.register(Route)
admin.site.register(ClimbingUserRoute)

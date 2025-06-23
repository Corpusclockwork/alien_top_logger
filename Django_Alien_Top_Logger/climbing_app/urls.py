from django.urls import path, include

from .views import ClimbingUserList, RouteList, ClimbingUserRouteList
 
urlpatterns = [
    path('climbingusers/', ClimbingUserList.as_view()),
    path('routes/', RouteList.as_view()),
    path('climbinguserroute/', ClimbingUserRouteList.as_view())
]

from django.urls import path, include

from .views import ClimbingUserList, RouteList, CreateRoutesList, ClimbingUserRouteList
 
urlpatterns = [
    path('climbingusers/', ClimbingUserList.as_view()),
    path('routes/', RouteList.as_view()),
    path('routes/create', CreateRoutesList.as_view(), name='createRoutes'),
    path('climbinguserroute/', ClimbingUserRouteList.as_view())
]

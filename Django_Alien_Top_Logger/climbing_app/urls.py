from django.urls import path, include

from .views import ClimbingUserList, RouteList, CreateRoutesList, DeleteRoutesList, ClimbingUserRouteList
 
urlpatterns = [
    path('climbingusers/', ClimbingUserList.as_view()),
    path('routes/', RouteList.as_view()),
    path('routes/create', CreateRoutesList.as_view(), name='createRoutes'),
    path('routes/delete', DeleteRoutesList.as_view(), name='deleteRoutes'),
    path('climbinguserroute/', ClimbingUserRouteList.as_view())
]

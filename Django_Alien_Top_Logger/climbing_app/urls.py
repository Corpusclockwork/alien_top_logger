from django.urls import path, include

from .views import ClimbingUserList, RouteList
 
urlpatterns = [
    path('climbingusers/', ClimbingUserList.as_view()),
    path('routes/', RouteList.as_view())
]

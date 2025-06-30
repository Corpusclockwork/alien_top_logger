from django.urls import path, include

from .views import AddUser, RouteList, CreateRoutes, DeleteRoutes
 
urlpatterns = [
    path('newuser/', AddUser.as_view()),
    path('routes/', RouteList.as_view()),
    path('routes/create', CreateRoutes.as_view(), name='createRoutes'),
    path('routes/delete', DeleteRoutes.as_view(), name='deleteRoutes')
]

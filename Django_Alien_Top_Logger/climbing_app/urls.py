from django.urls import path

from . import views

urlpatterns = [
    path('routes/', views.route_list, name='routes'),
    path('routes/create/', views.create_routes, name='createroutes'),
    path('routes/delete/', views.delete_routes, name='deleteroutes'),

    path('csrf/', views.get_csrf, name='csrf'),
    path('newuser/', views.add_user, name='newuser'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('session/', views.is_user_authenticated, name='usersession'),
]

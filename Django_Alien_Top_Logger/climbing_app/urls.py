from django.urls import path

from . import views

urlpatterns = [
    path('routes/', views.route_list, name='routes'),
    path('routes/create/', views.create_routes, name='createroutes'),
    path('routes/delete/', views.delete_routes, name='deleteroutes'),
    path('routes/track/', views.track_routes, name='trackroutes'),

    path('newuser/', views.add_user, name='newuser'),
    path('accounts/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('session/', views.session, name='usersession'),
]

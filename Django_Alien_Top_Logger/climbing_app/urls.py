from django.urls import path

from . import views

urlpatterns = [
    path('routes/', views.route_list, name='routes'),
    path('routes/getuserroutes/', views.get_routes_tracked_by_user, name='getroutestrackedbyuser'),
    path('routes/create/', views.create_routes, name='createroutes'),
    path('routes/delete/', views.delete_routes, name='deleteroutes'),
    path('routes/track/', views.track_routes, name='trackroutes'),

    path('newuser/', views.add_user, name='newuser'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('session/', views.session, name='usersession'),
    path('whoami/', views.who_am_i, name='whoami'),
]

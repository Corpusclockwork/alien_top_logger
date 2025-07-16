from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
# from rest_framework.response import Response

from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Route
from .serializers import RouteSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import permission_required
# Permissions normally enforced in this layer
    
#------- User -----------------------------------------
@require_POST
@csrf_exempt
def add_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    isClimbingStaffMemberInFrontEnd = data.get('isClimbingStaffMember')
    try:
        User.objects.get(username = username)
        return JsonResponse({
                'userExisted': True,
                'userCreated': False,
                'status': status.HTTP_403_FORBIDDEN
            })
    except:
        user = User.objects.create_user(username, None, password)
        print(user)
        if isClimbingStaffMemberInFrontEnd == True :
            group = Group.objects.get(name = 'isClimbingStaffMember')
            user.groups.add(group)
            user.save()
        else :
            group = Group.objects.get(name = 'isClimbingCustomer')
            user.groups.add(group)
            user.save()
        return JsonResponse({
                'userExisted': False,
                'userCreated': True,
                'status': status.HTTP_201_CREATED
            })
    
@ensure_csrf_cookie
def is_user_authenticated(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    return JsonResponse({
            'isAuthenticated': True,
            'isClimbingStaffMember': request.user.groups.filter(name="isClimbingStaffMember").exists(),
            'username': request.user.username
        })

#------- Login and Logout User -----------------------------------------
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

@require_POST
def login_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)
    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    login(request, user)
    return JsonResponse({
            'detail': 'Successfully logged in.',
            'isClimbingStaffMember': user.groups.filter(name="isClimbingStaffMember").exists()
        }, status=status.HTTP_202_ACCEPTED)
    
# @require_POST
def logout_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
    print(request.user)
    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'}, status=status.HTTP_202_ACCEPTED)
    
#------- Routes -----------------------------------------
@require_GET
def route_list(self):
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return JsonResponse({'routes': serializer.data})

@require_POST
@permission_required("can_add_routes")
def create_routes(request):
    serializer = RouteSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_required("can_delete_routes")
def delete_routes(request):
    Route.objects.filter(RouteId__in=request.data).delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)

@permission_required("can_track_routes")
def track_routes(request):
    data = json.loads(request.body)
    routeId = data.get('routeId')
    route_list(routeId).RoutesClimbedByUsers.add(request.userId)
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)
          
          
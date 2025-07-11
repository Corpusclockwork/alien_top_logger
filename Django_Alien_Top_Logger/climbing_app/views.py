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
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST, require_GET, require_safe
# Permissions normally enforced in this layer
    
#------- User -----------------------------------------
@require_POST
def add_user(request):
    try:
        User.objects.get(username = request.data["username"])
        return JsonResponse(data="Username already exists", status=status.HTTP_403_FORBIDDEN)
    except:
        user = User.objects.create_user(request.data["username"], request.data["email"], request.data["password"])
        if request.data["isClimbingStaffMemberInFrontEnd"] == True :
            group = Group.objects.get(name = 'isClimbingStaffMember')
            user.groups.add(group)
            user.save()
        return JsonResponse(status=status.HTTP_201_CREATED)
    
@ensure_csrf_cookie
def is_user_authenticated(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    return JsonResponse({'isAuthenticated': True, 'username': request.user.username})

#------- Login and Logout User -----------------------------------------
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

@require_POST
def login_user(request):
    print(request)
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)
    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'}, status=status.HTTP_202_ACCEPTED)
    
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
def create_routes(request):
    # permission_classes = (permissions.can_add_routes)
    serializer = RouteSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def delete_routes(request):
    # permission_classes = (permissions.can_delete_routes)
    Route.objects.filter(RouteId__in=request.data).delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)
          
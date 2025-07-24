from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
# from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Route
from .serializers import RouteSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, csrf_protect, requires_csrf_token
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import permission_required, login_required
# Permissions normally enforced in this layer
    
#------- User Authentication-----------------------------------------
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
def session(request):
    return JsonResponse({"CSRFTokenSet": True})

def who_am_i(request):
    print(request)
    if not request.user.is_authenticated:
        return JsonResponse({
            'isAuthenticated': False, 
        })
    return JsonResponse({
            'isAuthenticated': True,
            'username': request.user.username,
            'isClimbingStaffMember': request.user.groups.filter(name="isClimbingStaffMember").exists(),
        })

#------- Login and Logout User -----------------------------------------
def login_user(request):
    data = json.loads(request.body)
    print(data)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)
    print(user)
    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
    else :
        login(request, user)
        return JsonResponse({'detail': 'Successfully logged in.'}, status=status.HTTP_202_ACCEPTED)
    
def logout_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You are not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'}, status=status.HTTP_202_ACCEPTED)
    
#------- Routes -----------------------------------------
#get
def route_list(self):
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return JsonResponse({'routes': serializer.data})

def route_grade_ranges(self):
    # we just need the label in the front end, choices are (value, label) tuples
    return JsonResponse({'gradeRanges': [choice[1] for choice in Route.RouteGradeRangeClass.choices]})

def route_hold_colours(self):
    # we just need the label in the front end, choices are (value, label) tuples
    return JsonResponse({'holdColours': [choice[1] for choice in Route.RouteColourClass.choices]})
#------- Add Delete Routes -----------------------------------------
#post
# @permission_required("can_add_routes")
def create_routes(request):
    data = json.loads(request.body)
    print(data)
    serializer = RouteSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'routesCreated': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# @permission_required("can_delete_routes")
def delete_routes(request):
    data = json.loads(request.body)
    print(data)
    Route.objects.filter(RouteId__in=data).delete()
    return JsonResponse({'routesDeleted': data},status=status.HTTP_204_NO_CONTENT)

#------- Track Routes -----------------------------------------
# post
# @permission_required("can_track_routes")
def track_routes(request):
    data = json.loads(request.body)
    username = data.get('username')
    routeIdsToAdd = data.get('routesClimbedByUser')
    routesToTrack = Route.objects.filter(RouteId__in=routeIdsToAdd)
    for route in routesToTrack:
        route.RoutesClimbedByUsers.add(User.objects.get(username = username))
    return JsonResponse({'routesTrackedAdd': routeIdsToAdd},status=status.HTTP_201_CREATED)

#get
# @permission_required("can_track_routes")
def get_routes_tracked_by_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    print(username)
    routesSent = Route.objects.filter(RoutesClimbedByUsers = User.objects.get(username = username))
    serializer = RouteSerializer(data=routesSent, many=True)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse({'routesClimbedByUser': serializer.data})
          
          
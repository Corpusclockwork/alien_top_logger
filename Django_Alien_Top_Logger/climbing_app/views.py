from django.http.response import JsonResponse
import json
from rest_framework import status
from .models import Route
from .serializers import RouteSerializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import permission_required
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
        return JsonResponse({'status': status.HTTP_403_FORBIDDEN})
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
        return JsonResponse({'status': status.HTTP_201_CREATED})

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
@require_POST
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
@require_GET
def route_list(self):
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return JsonResponse({'routes': serializer.data})

@require_GET
def route_grade_ranges(self):
    return JsonResponse({'gradeRangeChoices': Route.RouteGradeRangeClass.choices})

@require_GET
def route_hold_colours(self):
    return JsonResponse({'holdColourChoices': Route.RouteColourClass.choices})

#------- Add Delete Routes -----------------------------------------
@require_POST
@permission_required("climbing_app.can_add_routes", raise_exception=True)
def create_routes(request):
    data = json.loads(request.body)
    print(data)
    serializer = RouteSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'routesCreated': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@require_POST
@permission_required("climbing_app.can_delete_routes", raise_exception=True)
def delete_routes(request):
    data = json.loads(request.body)
    print(data)
    Route.objects.filter(RouteId__in=data).delete()
    return JsonResponse({'routesDeleted': data},status=status.HTTP_204_NO_CONTENT)

#------- Track Routes -----------------------------------------
@require_POST
@permission_required("climbing_app.can_track_routes", raise_exception=True)
def track_routes(request):
    data = json.loads(request.body)
    username = data.get('username')
    routeIdsToAdd = data.get('routesClimbedByUser')
    routesToTrack = Route.objects.filter(RouteId__in=routeIdsToAdd)
    for route in routesToTrack:
        route.RoutesClimbedByUsers.add(User.objects.get(username = username))
    return JsonResponse({'routesTrackedAdd': routeIdsToAdd},status=status.HTTP_201_CREATED)

@permission_required("climbing_app.can_track_routes",  raise_exception=True)
def get_routes_tracked_by_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    routesSent = Route.objects.filter(RoutesClimbedByUsers = User.objects.get(username = username))
    serializer = RouteSerializer(data=routesSent, many=True)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse({'routesClimbedByUser': serializer.data})
                    
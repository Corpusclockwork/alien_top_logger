from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from .models import ClimbingUser, Route, ClimbingUserRoute
from .serializers import ClimbingUserSerializer, RouteSerializer, ClimbingUserRouteSerializer
from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# @api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
# @csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class ClimbingUserList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        climbingUsers = ClimbingUser.objects.all()
        serializer = ClimbingUserSerializer(climbingUsers, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class RouteList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)
    
class ClimbingUserRouteList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        ClimbingUserRoutes = ClimbingUserRoute.objects.all()
        serializer = ClimbingUserRouteSerializer(ClimbingUserRoutes, many=True)
        return Response(serializer.data)

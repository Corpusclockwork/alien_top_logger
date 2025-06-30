from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
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
    
class CreateRoutesList(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        #Deserialize incoming 350N data
        serializer = RouteSerializer(data=request.data, many=True)
        #Check if data is valid
        if serializer.is_valid():
            #Save the new routes to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
           #Return validation errors if data is invalid
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteRoutesList(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request):
        Route.objects.filter(RouteId__in=request.data).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
class ClimbingUserRouteList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        ClimbingUserRoutes = ClimbingUserRoute.objects.all()
        serializer = ClimbingUserRouteSerializer(ClimbingUserRoutes, many=True)
        return Response(serializer.data)

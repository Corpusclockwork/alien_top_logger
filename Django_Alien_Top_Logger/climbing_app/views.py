from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Route
from .serializers import RouteSerializer
from django.http.response import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
# Permissions nomrally enforced in this layer
    
#------- User -----------------------------------------
class AddUser(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        user = User.objects.create_user(request.data.username, request.data.email, request.data.password)
        group = Group.objects.get(name = 'isClimbingCustomer')
        user.groups.add(group)
        user.save()
        Response(status=status.HTTP_201_CREATED)
    
# class AuthenticatingUser(APIView):
#     def get(self, request):
#         user = authenticate(request.username, request.password)
#         if user is not None:
#             # A backend authenticated the credentials
#             return JsonResponse(status.HTTP_100_CONTINUE)
#         else:
#             # No backend authenticated the credentials
#             return JsonResponse(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    
#------- Route -----------------------------------------
class RouteList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

class CreateRoutes(APIView):
    # permission_classes = (permissions.can_add_routes)
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RouteSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteRoutes(APIView):
    permission_classes = (AllowAny,)
    # permission_classes = (permissions.can_delete_routes)
    def delete(self, request):
        Route.objects.filter(RouteId__in=request.data).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
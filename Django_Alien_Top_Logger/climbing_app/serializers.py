from rest_framework import serializers
from .models import ClimbingUser, Route, ClimbingUserRoute

class ClimbingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimbingUser
        fields = (
            "ClimbingUserId",
            "ClimbingUserName",
            "ClimbingUserPassword",
            "ClimbingUserCreatedAt"
        )

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            "RouteId",
            "RouteLocationXAxis",
            "RouteLocationYAxis",
            "RouteColour",
            "RouteGradeRange",
            "RouteCreatedAt",
            "RouteDestroyedAt"
        )

class ClimbingUserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimbingUserRoute
        fields = (
            "ClimbingUserId",
            "RouteId",
            "DateSent"
        )
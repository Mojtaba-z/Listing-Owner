from django.shortcuts import render
from rest_framework import viewsets, status
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import (
    Property,
    PropertyType,
    Room,
    RoomOptions,
    Amenities
)
from .serializers import (
    PropertySerializer,
    PropertyTypeSerializer,
    RoomSerializer,
    RoomOptionsSerializer,
    AmenitiesSerializer
)


# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [AllowAny]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]


class RoomOptionsViewSet(viewsets.ModelViewSet):
    queryset = RoomOptions.objects.all()
    serializer_class = RoomOptionsSerializer
    permission_classes = [AllowAny]


class AmenitiesViewSet(viewsets.ModelViewSet):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer
    permission_classes = [AllowAny]

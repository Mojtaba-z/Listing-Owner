from django.shortcuts import render
from rest_framework import viewsets, status
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import UserProfile
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
    """
        view set for manage properties create, update, remove, list, retrieve
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # contains userprofile object
        userprofile = UserProfile.objects.get(user_id=1)  # we should use request.user to identify user
        request.data['owner_id'] = userprofile.id
        amenities = request.data.pop('property_amenities')  # remove amenities ids list from request data
        rooms = request.data.pop('room')  # remove rooms ids list from request data

        # send data to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            property_obj = serializer.create(validated_data=request.data)  # contains property object
            property_obj.property_amenities.add(*amenities)
            property_obj.room.add(*rooms)
            serializer = self.serializer_class(property_obj)
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'result': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PropertyTypeViewSet(viewsets.ModelViewSet):
    """
        view set for manage property types create, update, remove, list, retrieve
    """
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [AllowAny]


class RoomViewSet(viewsets.ModelViewSet):
    """
        view set for manage rooms create, update, remove, list, retrieve
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]


class RoomOptionsViewSet(viewsets.ModelViewSet):
    """
        view set for manage room options create, update, remove, list, retrieve
    """
    queryset = RoomOptions.objects.all()
    serializer_class = RoomOptionsSerializer
    permission_classes = [AllowAny]


class AmenitiesViewSet(viewsets.ModelViewSet):
    """
        view set for manage amenities create, update, remove, list, retrieve
    """
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer
    permission_classes = [AllowAny]

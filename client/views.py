from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, status
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import UserProfile
from .models import Reservation
from .serializers import ReservationSerializer
from property_owner.models import Room


# Create your views here.


class ReservationViewSet(viewsets.ModelViewSet):
    """
        view set for manage reservations create, update, remove, list, retrieve by client
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # contains userprofile object
        userprofile = UserProfile.objects.get(user__id=1)  # we should use request.user to identify user
        request.data['guest_id'] = userprofile.id

        room_ids = request.data.pop('rooms_id') if 'rooms_id' in request.data.keys() else None

        # send data to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reservation_obj = serializer.create(validated_data=request.data)  # contains agent listing object
            if room_ids is not None:
                rooms_list = [
                    item for item in Room.objects.filter(id__in=room_ids) if item in reservation_obj.property.room.all()
                ]
                if rooms_list:
                    reservation_obj.room.add(*room_ids)
                    Room.objects.filter(id__in=room_ids).update(room_status="reserved")
                else:
                    return Response({'message': "room is not for this property"}, status=status.HTTP_404_NOT_FOUND)
                reservation_obj.property.property_status = "room_reserve"  # change property status
                reservation_obj.property.save()
                reservation_obj.reservation_type = "room_reserve"  # change reservation type
                reservation_obj.save()
            else:
                reservation_obj.property.property_status = "reserved"  # change property status
                reservation_obj.property.save()
            serializer = self.serializer_class(reservation_obj)
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'result': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

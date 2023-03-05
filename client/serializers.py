from rest_framework import serializers
from .models import Reservation
from property_owner.models import Property
from property_owner.serializers import PropertySerializer, RoomSerializer
from core.models import UserProfile
from core.serializers import UserProfileSerializer


class ReservationSerializer(serializers.ModelSerializer):
    guest_id = serializers.PrimaryKeyRelatedField(
        source='guest',
        queryset=UserProfile.objects.all()
    )
    guest = UserProfileSerializer(required=False)
    property_id = serializers.PrimaryKeyRelatedField(
        source='property',
        queryset=Property.objects.all()
    )
    property = PropertySerializer(required=False)
    room = RoomSerializer(required=False, many=True)

    class Meta:
        model = Reservation
        fields = '__all__'

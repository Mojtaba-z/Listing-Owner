from rest_framework import serializers
from .models import (
    Property,
    PropertyType,
    Room,
    RoomOptions,
    Amenities
)
from core.models import (
    UserProfile,
    Country,
    City
)
from core.serializers import (
    UserProfileSerializer,
    CountrySerializer,
    CitySerializer
)


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = (
            'id',
            'title',
        )


class RoomOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomOptions
        fields = (
            'id',
            'kind_of_beds',
            'number_of_beds',
            'capacity_of_guests',
        )


class RoomSerializer(serializers.ModelSerializer):
    room_options_id = serializers.PrimaryKeyRelatedField(
        source='room_options',
        queryset=RoomOptions.objects.all()
    )
    room_options = RoomOptionsSerializer(required=False)

    class Meta:
        model = Room


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = (
            'id',
            'title'
        )


class PropertySerializer(serializers.ModelSerializer):
    userprofile_id = serializers.PrimaryKeyRelatedField(
        source='userprofile',
        queryset=UserProfile.objects.all()
    )
    userprofile = UserProfileSerializer(required=False)
    property_type_id = serializers.PrimaryKeyRelatedField(
        source='property_type',
        queryset=PropertyType.objects.all()
    )
    property_type = PropertyTypeSerializer(required=False)
    property_amenities = AmenitiesSerializer(required=False, many=True)
    room = RoomSerializer(required=False, many=True)
    country_id = serializers.PrimaryKeyRelatedField(
        source='country',
        queryset=Country.objects.all()
    )
    country = CountrySerializer(required=False)
    city_id = serializers.PrimaryKeyRelatedField(
        source='city',
        queryset=City.objects.all()
    )
    city = CitySerializer(required=False)

    class Meta:
        model = Property
        fields = '__all__'

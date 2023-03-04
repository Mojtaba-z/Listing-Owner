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
        fields = '__all__'


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = (
            'id',
            'title'
        )


class PropertySerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(
        source='owner',
        queryset=UserProfile.objects.all()
    )
    owner = UserProfileSerializer(required=False)
    property_type_id = serializers.PrimaryKeyRelatedField(
        source='property_type',
        queryset=PropertyType.objects.all()
    )
    property_type = serializers.SerializerMethodField('get_property_type')
    property_amenities = AmenitiesSerializer(required=False, many=True)
    room = RoomSerializer(required=False, many=True)
    country_id = serializers.PrimaryKeyRelatedField(
        source='country',
        queryset=Country.objects.all()
    )
    country = serializers.SerializerMethodField('get_country')
    city_id = serializers.PrimaryKeyRelatedField(
        source='city',
        queryset=City.objects.all()
    )
    city = serializers.SerializerMethodField('get_city')

    class Meta:
        model = Property
        fields = '__all__'

    def get_city(self, instance):
        if instance.city:
            return instance.city.name
        else:
            return ""

    def get_country(self, instance):
        if instance.country:
            return instance.country.name
        else:
            return ""

    def get_property_type(self, instance):
        if instance.property_type:
            return instance.property_type.title
        else:
            return ""

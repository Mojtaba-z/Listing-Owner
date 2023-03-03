from rest_framework import serializers
from .models import (
    UserProfile,
    Country,
    City,
)
from django.contrib.auth.models import Group


class UserProfileSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        source='role',
        queryset=Group.objects.all()
    )
    role = serializers.SerializerMethodField('get_role')

    class Meta:
        model = UserProfile
        exclude = (
            'user',
        )

    def get_role(self, instance):
        if instance.role:
            return instance.role.name
        else:
            return ""


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'name',
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )

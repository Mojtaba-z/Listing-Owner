from rest_framework import serializers
from .models import AgentListings
from core.models import UserProfile
from core.serializers import (
    UserProfileSerializer,
)
from property_owner.serializers import PropertySerializer


class AgentListingsSerializer(serializers.ModelSerializer):
    agent_id = serializers.PrimaryKeyRelatedField(
        source='agent',
        queryset=UserProfile.objects.all()
    )
    agent = UserProfileSerializer(required=False)
    property = PropertySerializer(required=False, many=True)

    class Meta:
        model = AgentListings
        fields = (
            'id',
            'agent',
            'agent_id',
            'property',
            'title'
        )

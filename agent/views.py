from django.shortcuts import render
from rest_framework import viewsets, status
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import UserProfile
from .models import AgentListings
from .serializers import AgentListingsSerializer


# Create your views here.


class AgentListingsViewSet(viewsets.ModelViewSet):
    """
        view set for manage agent listings create, update, remove, list, retrieve
    """
    queryset = AgentListings.objects.all()
    serializer_class = AgentListingsSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # contains userprofile object
        userprofile = UserProfile.objects.get(user__id=1)  # we should use request.user to identify user
        request.data['agent_id'] = userprofile.id
        properties = request.data.pop('property')

        # send data to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            agent_listing_obj = serializer.create(validated_data=request.data)  # contains agent listing object
            agent_listing_obj.property.add(*properties)
            serializer = self.serializer_class(agent_listing_obj)
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'result': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

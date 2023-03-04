from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets, status
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.models import UserProfile
from .models import AgentListings
from .serializers import AgentListingsSerializer
from property_owner.models import Property
from property_owner.serializers import PropertySerializer
import pytz


utc = pytz.UTC

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


class ManageProperties(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], name="Get detail of properties that are available at a certain time")
    def available_properties(self, request):
        certain_date = datetime.strptime(request.data['date'], "%Y-%m-%d")  # convert string to date
        available_property_list = []
        for property_item in self.queryset:
            if property_item.property_reservation.all():  # check if a property has reservation
                for item in property_item.property_reservation.all():
                    if not item.start_date <= utc.localize(certain_date) <= item.end_date:
                        if property_item not in available_property_list:  # prevent from repeat adding same objects
                            available_property_list.append(property_item)
                    else:
                        pass
            else:
                available_property_list.append(property_item)

        # serialize property objects
        serializer = self.serializer_class(available_property_list, many=True)
        return Response({'result': serializer.data}, status=status.HTTP_200_OK)


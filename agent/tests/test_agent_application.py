from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import AgentListings
from property_owner.models import Property, Room
from core.models import User, UserProfile
from client.models import Reservation
from datetime import datetime


class TestAgentListing(APITestCase):
    url = '/agent/agent_listings/'

    def setUp(self):
        # Prepare Setup For Tests
        User.objects.create(id=1)
        UserProfile.objects.create(id=1, user_id=1)
        Property.objects.create(id=1, property_name='Amazon Property')
        AgentListings.objects.create(title='list 1', agent_id=1).property.add(1)

    def test_post_agent_listing(self):
        # definition
        data = {
            "title": "list 1",
            "property": [1]
        }
        # process
        response = self.client.post(self.url, data, format='json')

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_agents(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestManageProperties(APITestCase):
    url = '/agent/manage_properties/'

    def setUp(self) -> None:
        User.objects.create(id=1)
        UserProfile.objects.create(id=1, user_id=1)
        Room.objects.create(id=1, room_name='Studio Room')
        Property.objects.create(id=1, property_name='Amazon Property').room.add(1)
        start_date = datetime.strptime("2022-03-22", "%Y-%m-%d")
        end_date = datetime.strptime("2022-05-22", "%Y-%m-%d")

        # for available properties
        Reservation.objects.create(
            guest_id=1,
            start_date=start_date,
            end_date=end_date,
            property_id=1,
            reservation_status=True,
            reservation_type="property"
        )

        # for available rooms of a property
        Reservation.objects.create(
            guest_id=1,
            start_date=start_date,
            end_date=end_date,
            property_id=1,
            reservation_status=True,
            reservation_type="room_reserve"
        ).room.add(1)

    def test_available_properties(self):
        url = self.url + 'available_properties/'
        # definition
        data = {
            "date": "2022-06-10"
        }
        # process
        response = self.client.post(url, data, format='json')

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_available_rooms(self):
        url = self.url + 'available_rooms/'
        # definition
        data = {
            "date": "2022-06-10"
        }
        # process
        response = self.client.post(url, data, format='json')

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

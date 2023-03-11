from rest_framework.test import APITestCase
from rest_framework import status
from core.models import UserProfile, User
from property_owner.models import Property, Room
from ..models import Reservation


class TestReservation(APITestCase):
    url = '/client/reservation/'

    def setUp(self) -> None:
        User.objects.create(id=1)
        UserProfile.objects.create(id=1, user_id=1, first_name='Mojtaba')
        Room.objects.create(id=1, room_name='Studio Room')
        Property.objects.create(id=1, property_name='Amazon Property').room.add(1)
        Reservation.objects.create(special_request='i want cool water')

    def test_post_property_reservation(self):
        # definition
        data = {
            "special_request": "i want two beds",
            "start_date": "2022-05-21 02:20:15",
            "end_date": "2022-06-21 02:20:15",
            "guest_arrival_time": "2022-05-25 02:20:15",
            "property_id": 1,
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

    def test_post_room_reservation(self):
        # definition
        data = {
            "special_request": "i want two beds",
            "start_date": "2022-05-21 02:20:15",
            "end_date": "2022-06-21 02:20:15",
            "guest_arrival_time": "2022-05-25 02:20:15",
            "property_id": 1,
            "rooms_id": [1]
        }
        # process
        response = self.client.post(self.url, data, format='json')

        """print response output"""
        print("***")
        print(response.json())
        print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reservation(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

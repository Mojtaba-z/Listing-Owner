from rest_framework.test import APITestCase
from rest_framework import status
from core.models import UserProfile
from property_owner.models import (
    Property,
    PropertyType,
    Country,
    City,
    Amenities,
    Room, RoomOptions
)
from django.contrib.auth.models import User
import json


class TestProperty(APITestCase):
    """
        Test Property Apis by TestCase
    """
    url = '/property_owner/property/'

    def setUp(self):
        user = User.objects.create(id=1)
        UserProfile.objects.create(id=1, user=user)
        PropertyType.objects.create(id=1)
        Property.objects.create(
            owner_id=1,
            property_name='Amazon property',
            property_type_id=1,
            street_address='street number 2'
        )
        Country.objects.create(id=1)
        City.objects.create(id=1)
        Amenities.objects.create(id=1)
        Room.objects.create(id=1)

    def test_post_property(self):
        # definition
        data = {
            "property_name": "property number 1",
            "property_type_id": 1,
            "property_amenities": [1],
            "room": [1],
            "street_address": "cansas street 2",
            "address_line": "street line 2",
            "country_id": 1,
            "city_id": 1,
            "zip_code": "656689",
            "price_per_night": 3000,
            "property_status": "unreserved"
        }
        # process
        response = self.client.post(self.url, data, format='json')

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # we use response.user = User.objects.get(id=1) if want to identify user by request.user in api(or view set)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_property(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_property(self):
        # update property objects
        pass

    def test_delete_property(self):
        # delete property objects
        pass


class TestPropertyType(APITestCase):
    url = '/property_owner/property_type/'

    def setUp(self):
        PropertyType.objects.create(title='camp')

    def test_post_property_type(self):
        # definition
        data = {
            "title": "camp"
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

    def test_get_property_type(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_property_type(self):
        # update property type objects
        pass

    def test_delete_property_type(self):
        # delete property type objects
        pass


class TestRoom(APITestCase):
    url = '/property_owner/room/'

    def setUp(self):
        RoomOptions.objects.create(id=1, number_of_beds=2)
        Room.objects.create(room_name='Amazon Room', room_options_id=1)

    def test_post_room(self):
        # definition
        data = {
            "room_name": "room number 2",
            "room_size": "6*6",
            "room_options_id": 1,
            "room_status": "unreserved"
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

    def test_get_room(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_room(self):
        # update room objects
        pass

    def test_delete_room(self):
        # remove room objects
        pass


class TestRoomOptions(APITestCase):
    url = '/property_owner/room_options/'

    def setUp(self):
        RoomOptions.objects.create(number_of_beds=2, kind_of_beds="kind 1")

    def test_post_room_options(self):
        # definition
        data = {
            "kind_of_beds": "kind 2",
            "number_of_beds": 2,
            "capacity_of_guests": 2
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

    def test_get_room_options(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_room_options(self):
        # update room option objects
        pass

    def test_delete_room_options(self):
        # remove room option objects
        pass


class TestAmenities(APITestCase):
    url = '/property_owner/amenities/'

    def setUp(self):
        Amenities.objects.create(title="balcony")

    def test_post_amenities(self):
        # definition
        data = {
            "title": "balcony"
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

    def test_get_amenities(self):
        # process
        response = self.client.get(self.url)

        """print response output"""
        # print("***")
        # print(response.json())
        # print("***")
        """---------------------"""

        # response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_amenities(self):
        pass

    def test_delete_amenities(self):
        pass

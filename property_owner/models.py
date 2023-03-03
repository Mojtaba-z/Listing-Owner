from django.db import models
from core.models import (
    BaseModel,
    UserProfile,
    Country,
    City
)


# Create your models here.

class Property(BaseModel):
    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='property_owner',
        null=True
    )
    property_name = models.CharField(max_length=300, null=True)
    property_type = models.ForeignKey(
        'PropertyType',
        on_delete=models.CASCADE,
        related_name='property_type'
    )
    property_amenities = models.ManyToManyField(
        'Amenities',
        related_name='property_amenities'
    )
    room = models.ManyToManyField(
        'Room',
        related_name='property_room'
    )
    street_address = models.CharField(max_length=200, null=True)
    address_line = models.CharField(max_length=400, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='property_country',
        null=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='property_city',
        null=True
    )
    property_photos = models.JSONField(default=dict)
    zip_code = models.CharField(max_length=50, null=True)
    price_per_night = models.BigIntegerField(default=0)
    property_status = models.CharField(max_length=50, default='unreserved')

    def save(self, *args, **kwargs):
        super(Property, self).save(*args, **kwargs)


class PropertyType(BaseModel):
    title = models.CharField(max_length=150, null=True)

    def save(self, *args, **kwargs):
        super(PropertyType, self).save(*args, **kwargs)


class Room(BaseModel):
    room_name = models.CharField(max_length=150, null=True)
    room_size = models.CharField(max_length=150, null=True)
    room_options = models.ForeignKey(
        'RoomOptions',
        on_delete=models.CASCADE,
        related_name='room_options',
        null=True
    )
    room_status = models.CharField(max_length=50, default='unreserved')

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)


class RoomOptions(BaseModel):
    kind_of_beds = models.CharField(max_length=500, null=True)
    number_of_beds = models.IntegerField(default=0)
    capacity_of_guests = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(RoomOptions, self).save(*args, **kwargs)


class Amenities(BaseModel):
    title = models.CharField(max_length=150, null=True)

    def save(self, *args, **kwargs):
        super(Amenities, self).save(*args, **kwargs)
from django.db import models
from datetime import datetime
from core.models import (
    BaseModel,
    UserProfile
)
from property_owner.models import Property
# Create your models here.


class Reservation(BaseModel):
    guest = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='guest_reservation',
        null=True
    )
    special_request = models.TextField(max_length=2000, null=True)
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())
    guest_arrival_time = models.DateTimeField(datetime.now())
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='property_reservation',
        null=True
    )
    reservation_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Reservation, self).save(*args, **kwargs)
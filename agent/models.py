from django.db import models
from core.models import (
    BaseModel,
    UserProfile
)
from property_owner.models import Property


# Create your models here.

class AgentListings(BaseModel):
    agent = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='agent_listings',
        null=True
    )
    title = models.CharField(max_length=300, null=True)
    property = models.ManyToManyField(
        Property,
        related_name='listings_property'
    )

    def save(self, *args, **kwargs):
        super(AgentListings, self).save(*args, **kwargs)

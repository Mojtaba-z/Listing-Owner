from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    Group,
    User
)
from datetime import datetime
import uuid


# Create your models here.
class BaseModel(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_modifiedby",
        null=True,
        blank=True,
    )
    trash = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True
    )
    username = models.CharField(max_length=150, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    fathers_name = models.CharField(max_length=150, null=True)
    national_id = models.CharField(max_length=20, null=True)
    birth_date = models.DateTimeField(default=datetime.now())
    mobile = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    profile_pic = models.CharField(max_length=300, null=True)
    role = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="user_roles",
        null=True
    )

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

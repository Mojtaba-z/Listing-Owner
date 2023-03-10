# Generated by Django 3.2.8 on 2023-03-03 07:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('trash', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, null=True)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('fathers_name', models.CharField(max_length=150, null=True)),
                ('national_id', models.CharField(max_length=20, null=True)),
                ('birth_date', models.DateTimeField(default=datetime.datetime(2023, 3, 3, 11, 19, 33, 723779))),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('profile_pic', models.CharField(max_length=300, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_roles', to='auth.group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

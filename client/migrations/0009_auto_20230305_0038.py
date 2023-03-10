# Generated by Django 3.2.8 on 2023-03-04 21:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_owner', '0004_roomoptions_number_of_beds'),
        ('client', '0008_auto_20230304_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_reservation', to='property_owner.room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 0, 38, 23, 304297)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_arrival_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 5, 0, 38, 23, 304297)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 0, 38, 23, 304297)),
        ),
    ]

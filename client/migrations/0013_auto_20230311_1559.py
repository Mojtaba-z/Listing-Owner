# Generated by Django 3.2.8 on 2023-03-11 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20230305_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 15, 59, 43, 263023)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 15, 59, 43, 263023)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 15, 59, 43, 263023)),
        ),
    ]

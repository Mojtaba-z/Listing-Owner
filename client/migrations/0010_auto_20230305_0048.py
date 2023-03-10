# Generated by Django 3.2.8 on 2023-03-04 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20230305_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_type',
            field=models.CharField(default='property', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 0, 48, 47, 835494)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_arrival_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 5, 0, 48, 47, 835494)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 0, 48, 47, 835494)),
        ),
    ]

# Generated by Django 3.2.8 on 2023-03-04 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 0, 48, 47, 817538)),
        ),
    ]

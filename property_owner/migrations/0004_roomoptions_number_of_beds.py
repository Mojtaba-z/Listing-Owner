# Generated by Django 3.2.8 on 2023-03-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_owner', '0003_alter_property_property_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomoptions',
            name='number_of_beds',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_roads_roadstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='RoadStatus',
            field=models.IntegerField(choices=[(0, 'No Traffic Delays'), (1, ' Medium Amount of Traffic'), (2, ' traffic delays')], default=0),
        ),
    ]

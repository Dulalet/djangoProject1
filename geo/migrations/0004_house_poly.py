# Generated by Django 3.1.5 on 2021-01-24 15:45

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20210124_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='poly',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
    ]

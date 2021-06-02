# Generated by Django 3.1.6 on 2021-04-05 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import osm_field.fields
import osm_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_number', models.CharField(blank=True, max_length=17)),
                ('address', models.CharField(blank=True, max_length=17)),
                ('crop_product', models.CharField(max_length=100)),
                ('usable_area', models.CharField(max_length=100)),
                ('soil_type', models.CharField(choices=[('clay', 'clay'), ('loamy', 'loamy'), ('sandy', 'sandy'), ('silty', 'silty')], default='clay', max_length=11)),
                ('ownership_type', models.CharField(choices=[('lease', 'lease'), ('private', 'private'), ('mixed', 'mixed'), ('other', 'other')], default='private', max_length=11)),
                ('location', osm_field.fields.OSMField(lat_field='location_lat', lon_field='location_lon')),
                ('location_lat', osm_field.fields.LatitudeField(validators=[osm_field.validators.validate_latitude])),
                ('location_lon', osm_field.fields.LongitudeField(validators=[osm_field.validators.validate_longitude])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
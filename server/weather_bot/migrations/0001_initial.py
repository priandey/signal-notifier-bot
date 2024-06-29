# Generated by Django 4.2.10 on 2024-06-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_datetime', models.DateTimeField(verbose_name='segment datetime')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='longitude')),
                ('data', models.JSONField(verbose_name='data')),
                ('average_temperature_celsius', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='average temperature in °c')),
                ('average_wind_speed', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='average wind speed')),
                ('wind_gust_speed', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='wind gust speed')),
                ('could_snow', models.BooleanField(verbose_name='could snow')),
                ('cloud_coverage', models.IntegerField(verbose_name='cloud_coverage %')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'indexes': [models.Index(fields=['segment_datetime'], name='weather_bot_segment_29130a_idx')],
            },
        ),
    ]
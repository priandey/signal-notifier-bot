# Generated by Django 4.2.10 on 2024-06-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_bot', '0003_weatheralertcondition_weatheralertconfiguration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatheralertcondition',
            name='left_operand',
            field=models.CharField(max_length=255, null=True, verbose_name='right operand'),
        ),
    ]
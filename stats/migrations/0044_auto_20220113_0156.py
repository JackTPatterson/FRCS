# Generated by Django 3.1.7 on 2022-01-13 01:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0043_auto_20220113_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 1, 56, 11, 219318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='stat_id',
            field=models.CharField(editable=False, max_length=15),
        ),
    ]
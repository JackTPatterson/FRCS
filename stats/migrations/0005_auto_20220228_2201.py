# Generated by Django 2.2.14 on 2022-02-28 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20220228_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_stats',
            name='archived',
        ),
        migrations.RemoveField(
            model_name='game_stats',
            name='comp',
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 22, 1, 39, 671659)),
        ),
    ]

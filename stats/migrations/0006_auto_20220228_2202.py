# Generated by Django 2.2.14 on 2022-02-28 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20220228_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_stats',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game_stats',
            name='comp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 22, 2, 11, 853545)),
        ),
    ]

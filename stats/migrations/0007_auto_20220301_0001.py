# Generated by Django 2.2.14 on 2022-03-01 00:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20220228_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_stats',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 0, 1, 15, 32813)),
        ),
    ]
# Generated by Django 2.2.14 on 2022-03-01 00:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_auto_20220301_0014'),
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
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game_stats',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 0, 33, 0, 648998)),
        ),
    ]

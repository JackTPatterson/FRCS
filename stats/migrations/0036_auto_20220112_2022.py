# Generated by Django 3.1.7 on 2022-01-12 20:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0035_auto_20220112_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 20, 22, 7, 713983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='team_num',
            field=models.PositiveIntegerField(),
        ),
    ]
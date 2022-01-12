# Generated by Django 3.1.7 on 2022-01-12 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0036_auto_20220112_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pit_stats',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 20, 24, 41, 911910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pit_stats',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

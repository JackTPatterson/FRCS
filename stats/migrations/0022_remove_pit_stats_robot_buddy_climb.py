# Generated by Django 3.1.7 on 2022-01-12 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_auto_20220112_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pit_stats',
            name='robot_buddy_climb',
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-01 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20191101_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_news',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 1, 12, 30, 38, 83522), verbose_name='Data pusblihed'),
        ),
        migrations.AlterField(
            model_name='updates',
            name='published_updates',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 1, 12, 30, 38, 84847), verbose_name='Data pusblihed'),
        ),
    ]

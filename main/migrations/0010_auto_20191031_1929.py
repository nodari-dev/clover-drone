# Generated by Django 2.1.5 on 2019-10-31 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191030_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_news',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 19, 29, 39, 362733), verbose_name='Data pusblihed'),
        ),
        migrations.AlterField(
            model_name='updates',
            name='published_updates',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 19, 29, 39, 364736), verbose_name='Data pusblihed'),
        ),
    ]

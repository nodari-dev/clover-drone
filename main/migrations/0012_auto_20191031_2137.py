# Generated by Django 2.1.5 on 2019-10-31 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20191031_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_news',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 21, 37, 11, 578760), verbose_name='Data pusblihed'),
        ),
        migrations.AlterField(
            model_name='updates',
            name='published_updates',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 21, 37, 11, 579761), verbose_name='Data pusblihed'),
        ),
    ]

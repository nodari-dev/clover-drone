# Generated by Django 2.1.5 on 2019-10-30 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191029_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_news',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 10, 32, 57, 720653), verbose_name='Data pusblihed'),
        ),
        migrations.AlterField(
            model_name='updates',
            name='published_updates',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 30, 10, 32, 57, 721654), verbose_name='Data pusblihed'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-16 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190816_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highscore',
            name='archived_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 12, 2, 33, 816298)),
        ),
        migrations.AlterField(
            model_name='options',
            name='is_correct',
            field=models.BooleanField(),
        ),
    ]

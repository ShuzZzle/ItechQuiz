# Generated by Django 2.2.4 on 2019-08-16 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190816_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highscore',
            name='archived_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 16, 6, 45, 182269)),
        ),
    ]
# Generated by Django 2.0 on 2017-12-18 01:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0010_auto_20171218_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 1, 11, 4, 819925)),
        ),
    ]

# Generated by Django 2.0 on 2017-12-18 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0008_auto_20171218_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 1, 3, 29, 569679)),
        ),
    ]

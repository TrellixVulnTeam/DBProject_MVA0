# Generated by Django 2.0 on 2017-12-18 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0006_auto_20171218_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 0, 40, 12, 505224)),
        ),
    ]

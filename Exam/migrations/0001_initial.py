# Generated by Django 2.0 on 2017-12-18 08:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pytz

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=280)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('time_of_creation', models.DateTimeField(default=datetime.datetime.now(pytz.timezone('US/Eastern')))),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=280)),
                ('number', models.CharField(max_length=3)),
                ('points', models.FloatField(default=1)),
                ('answers', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Exam.Answers')),
                ('examName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.TextField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Student'),
        ),
    ]

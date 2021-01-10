# Generated by Django 3.1.5 on 2021-01-09 23:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0013_auto_20210109_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='status',
        ),
        migrations.AddField(
            model_name='meal',
            name='arrived',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='consumed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meal',
            name='eat_by',
            field=models.DateField(default=datetime.datetime(2021, 1, 9, 23, 11, 52, 277931, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

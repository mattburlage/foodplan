# Generated by Django 3.1.5 on 2021-01-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0015_auto_20210109_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='arrival',
        ),
        migrations.AddField(
            model_name='meal',
            name='arrived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='meal',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20210109_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='expiration',
            field=models.DateField(blank=True, null=True),
        ),
    ]
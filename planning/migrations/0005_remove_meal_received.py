# Generated by Django 3.1.5 on 2021-01-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0004_meal_received'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='received',
        ),
    ]

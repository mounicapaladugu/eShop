# Generated by Django 2.2.2 on 2019-06-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location info', max_length=120),
        ),
    ]

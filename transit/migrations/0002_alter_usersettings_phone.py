# Generated by Django 4.0.3 on 2022-03-27 08:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('transit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]

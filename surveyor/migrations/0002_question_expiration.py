# Generated by Django 2.0 on 2017-12-23 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('surveyor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 23, 20, 26, 4, 389555, tzinfo=utc)),
        ),
    ]

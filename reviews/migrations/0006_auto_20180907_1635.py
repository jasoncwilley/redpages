# Generated by Django 2.0 on 2018-09-07 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20180907_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 7, 16, 35, 16, 957362), verbose_name='date created'),
        ),
    ]

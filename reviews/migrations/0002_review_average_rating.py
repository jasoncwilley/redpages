# Generated by Django 2.0 on 2018-09-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='average_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.0 on 2018-09-10 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180910_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name', to='company.CompanyByType', to_field='company_name'),
        ),
    ]

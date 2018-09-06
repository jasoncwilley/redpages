# Generated by Django 2.0 on 2018-09-06 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyByType')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('companyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.CompanyReviews')),
            ],
        ),
    ]

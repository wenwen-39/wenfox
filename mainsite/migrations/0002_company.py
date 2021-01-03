# Generated by Django 3.1.3 on 2020-12-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=1000)),
                ('place', models.CharField(default='M', max_length=1000)),
                ('people', models.CharField(default='M', max_length=1000)),
                ('car', models.CharField(blank=True, default='', max_length=1000)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]

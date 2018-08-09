# Generated by Django 2.1 on 2018-08-09 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(blank=True, max_length=200)),
                ('destination', models.CharField(blank=True, max_length=200)),
                ('depart_date', models.CharField(blank=True, max_length=100)),
                ('return_date', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlightInfoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=800)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flights.FlightInfo')),
            ],
        ),
    ]

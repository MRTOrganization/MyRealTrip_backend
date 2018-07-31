# Generated by Django 2.0.7 on 2018-07-31 08:20

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
                ('date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('price', models.CharField(blank=True, max_length=100)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flights.FlightInfo')),
            ],
        ),
    ]
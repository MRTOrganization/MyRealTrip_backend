# Generated by Django 2.1 on 2018-08-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KoreanHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('thumbnail', models.CharField(blank=True, max_length=255)),
                ('comments', models.CharField(blank=True, max_length=255)),
                ('price', models.CharField(blank=True, max_length=255)),
                ('detail_url', models.CharField(blank=True, max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Country')),
            ],
        ),
        migrations.CreateModel(
            name='KoreanHotelDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('pictures', models.CharField(blank=True, max_length=50000)),
                ('infos', models.CharField(blank=True, max_length=5000)),
                ('korean_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.KoreanHotel')),
            ],
        ),
        migrations.CreateModel(
            name='KoreanHotelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Country')),
            ],
        ),
    ]

# Generated by Django 2.1 on 2018-08-13 03:04

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
                ('name', models.CharField(blank=True, max_length=50)),
                ('thumbnail', models.ImageField(blank=True, upload_to='koreanhotel')),
                ('comments', models.CharField(blank=True, max_length=50)),
                ('price', models.CharField(blank=True, max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Country')),
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

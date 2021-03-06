# Generated by Django 2.1 on 2018-08-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccomSearchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction', models.CharField(blank=True, max_length=255)),
                ('checkin', models.CharField(blank=True, max_length=255)),
                ('checkout', models.CharField(blank=True, max_length=255)),
                ('group_adults', models.CharField(blank=True, max_length=255)),
                ('group_children', models.CharField(blank=True, max_length=255)),
                ('no_rooms', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AccomSearchInfoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=800)),
                ('accomsearch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accom_search.AccomSearchInfo')),
            ],
        ),
    ]

# Generated by Django 2.1 on 2018-08-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20180805_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_airline',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_arr_airport',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_arr_time',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_dep_airport',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_dep_time',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='go_flytime',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_airline',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_arr_airport',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_arr_time',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_dep_airport',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_dep_time',
        ),
        migrations.RemoveField(
            model_name='flightinfodetail',
            name='return_flytime',
        ),
        migrations.AddField(
            model_name='flightinfodetail',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightinfo',
            name='depart_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flightinfo',
            name='return_date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

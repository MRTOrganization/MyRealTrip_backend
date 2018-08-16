# Generated by Django 2.1 on 2018-08-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180813_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_info',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='tour_name',
            field=models.CharField(max_length=15),
        ),
    ]

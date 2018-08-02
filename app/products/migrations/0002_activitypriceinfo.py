# Generated by Django 2.0.7 on 2018-08-02 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('price', models.CharField(blank=True, max_length=100)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_price', to='products.ActivityInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

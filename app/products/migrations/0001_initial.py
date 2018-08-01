# Generated by Django 2.0.7 on 2018-07-31 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True)),
                ('date', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.ManyToManyField(related_name='city_activity', to='region.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuidePriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('price', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GuideTourInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True)),
                ('date', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=5)),
                ('region', models.ManyToManyField(related_name='city_guide', to='region.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TicketInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True)),
                ('date', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.ManyToManyField(related_name='city_ticket', to='region.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TicketPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('price', models.CharField(blank=True, max_length=100)),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_price', to='products.TicketInfo')),
            ],
        ),
        migrations.AddField(
            model_name='guidepriceinfo',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guide_price', to='products.GuideTourInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_by_guide_tour', to='products.GuideTourInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_by_tickets', to='products.TicketInfo'),
        ),
    ]

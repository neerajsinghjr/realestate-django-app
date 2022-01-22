# Generated by Django 3.2.11 on 2022-01-22 16:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=512)),
                ('descripton', models.TextField(blank=True)),
                ('top_seller', models.BooleanField(default=False)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('avatar', models.ImageField(blank='avatar.png', upload_to='avatar/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(blank='', max_length=20)),
                ('email', models.CharField(max_length=512)),
                ('descripton', models.TextField(blank=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('avatar', models.ImageField(blank='avatar.png', upload_to='avatar/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('pincode', models.CharField(max_length=32)),
                ('descripton', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photo_bg', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='listings/%Y/%m/%d/')),
                ('realtor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.realtor')),
            ],
        ),
    ]

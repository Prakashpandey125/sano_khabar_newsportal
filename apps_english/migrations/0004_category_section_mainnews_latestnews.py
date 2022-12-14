# Generated by Django 4.0.4 on 2022-06-23 06:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_english', '0003_remove_standardnews_date_time_picker'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='section',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('date_time_picker', models.DateTimeField(default=datetime.datetime.now)),
                ('number_of_views', models.BigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='0:processing, 1:completed')),
                ('standard_news', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_news', to='apps_english.standardnews')),
            ],
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('date_time_picker', models.DateTimeField(default=datetime.datetime.now)),
                ('number_of_views', models.BigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='0:processing, 1:completed')),
                ('standard_news', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='latest_news', to='apps_english.standardnews')),
            ],
        ),
    ]

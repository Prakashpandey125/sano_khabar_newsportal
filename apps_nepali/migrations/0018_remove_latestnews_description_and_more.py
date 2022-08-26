# Generated by Django 4.0.2 on 2022-08-26 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0017_auto_20220825_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestnews',
            name='description',
        ),
        migrations.RemoveField(
            model_name='latestnews',
            name='editor_name',
        ),
        migrations.RemoveField(
            model_name='latestnews',
            name='location',
        ),
        migrations.RemoveField(
            model_name='latestnews',
            name='news_summary',
        ),
        migrations.RemoveField(
            model_name='latestnews',
            name='photo_img',
        ),
        migrations.RemoveField(
            model_name='latestnews',
            name='title',
        ),
        migrations.AddField(
            model_name='latestnews',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
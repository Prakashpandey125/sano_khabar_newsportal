# Generated by Django 3.2.15 on 2022-08-25 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0014_remove_standardnews_date_time_picker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestnews',
            name='standard_news',
        ),
        migrations.RemoveField(
            model_name='mainnews',
            name='standard_news',
        ),
    ]

# Generated by Django 4.0.2 on 2022-08-10 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0006_alter_breakingnews_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo_img', models.ImageField(blank=True, default='default', null=True, upload_to='photos/Advertisement')),
                ('link', models.CharField(max_length=200)),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True, help_text='0:processing, 1:completed')),
            ],
        ),
    ]
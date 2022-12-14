# Generated by Django 3.2.15 on 2022-08-25 07:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0012_auto_20220825_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestnews',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' '),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='editor_name',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='location',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='news_summary',
            field=django_mysql.models.SizedTextField(null=True, size_class=2),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='photo_img',
            field=models.ImageField(blank=True, default='default', null=True, upload_to='photos/StandardNews'),
        ),
        migrations.AddField(
            model_name='latestnews',
            name='title',
            field=models.CharField(default='default', max_length=200),
        ),
    ]

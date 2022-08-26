# Generated by Django 4.0.4 on 2022-06-16 05:48

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True, help_text='0:processing, 1:completed')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='apps_nepali.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('editor_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('photo_img', models.ImageField(blank=True, default='default', null=True, upload_to='photos/StandardNews')),
                ('news_summary', django_mysql.models.SizedTextField(null=True, size_class=2)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(default=' ')),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('number_of_views', models.BigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='0:processing, 1:completed')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_category', to='apps_nepali.category')),
            ],
        ),
    ]

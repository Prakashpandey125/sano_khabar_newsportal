# Generated by Django 4.0.2 on 2022-08-28 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0019_addsubtitle_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsubtitle',
            name='category',
        ),
    ]
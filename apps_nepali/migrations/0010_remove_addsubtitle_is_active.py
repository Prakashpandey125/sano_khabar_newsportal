# Generated by Django 4.0.2 on 2022-08-15 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0009_addsubtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsubtitle',
            name='is_active',
        ),
    ]

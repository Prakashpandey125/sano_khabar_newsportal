# Generated by Django 4.0.2 on 2022-08-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_nepali', '0018_remove_latestnews_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addsubtitle',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ap_add_sub_title', to='apps_nepali.category'),
        ),
    ]
# Generated by Django 2.2.7 on 2020-05-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueweb', '0004_auto_20200419_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='hyperfollow',
            field=models.URLField(blank=True, null=True),
        ),
    ]

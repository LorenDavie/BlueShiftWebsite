# Generated by Django 2.2.7 on 2019-12-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueweb', '0002_auto_20191228_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='hosting',
            field=models.CharField(blank=True, choices=[('soundcloud', 'SoundCloud')], max_length=100),
        ),
    ]
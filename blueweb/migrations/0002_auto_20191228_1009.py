# Generated by Django 2.2.7 on 2019-12-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['ordering']},
        ),
        migrations.AddField(
            model_name='song',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
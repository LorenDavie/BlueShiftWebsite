# Generated by Django 2.2.7 on 2019-12-11 19:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('body', models.TextField(blank=True)),
                ('posted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('release_date', models.DateField()),
                ('cover_art', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-release_date',),
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('snippet', models.CharField(blank=True, max_length=500, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='blueweb.Release')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='blueweb.Venue')),
            ],
            options={
                'ordering': ('when',),
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoking', models.IntegerField(choices=[(0, 'Never smoked'), (1, 'Tried smoking'), (3, 'Former smoker'), (4, 'Current smoker')])),
                ('drinking', models.IntegerField(choices=[(0, 'Never'), (1, 'Social drinker'), (2, 'Drink a lot')])),
                ('health_lifesty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='spend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_all', models.IntegerField()),
                ('shopping_center', models.IntegerField()),
                ('branded_clothing', models.IntegerField()),
                ('partying_socializing', models.IntegerField()),
                ('appearance', models.IntegerField()),
                ('gadgets', models.IntegerField()),
                ('food', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userfeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enjoymusic', models.IntegerField()),
                ('enjoymovie', models.IntegerField()),
                ('hobbies', models.ManyToManyField(blank=True, to='search.hobbies')),
                ('moviehated', models.ManyToManyField(blank=True, related_name='hmovie', to='search.music')),
                ('movieloved', models.ManyToManyField(blank=True, related_name='lmovie', to='search.movie')),
                ('musichated', models.ManyToManyField(blank=True, related_name='hmusic', to='search.music')),
                ('musicloved', models.ManyToManyField(blank=True, related_name='lmusic', to='search.music')),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2021-11-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_panner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='panner',
            field=models.ImageField(upload_to='movies/panner'),
        ),
    ]

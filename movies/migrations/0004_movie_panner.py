# Generated by Django 3.1.2 on 2021-11-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20211120_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='panner',
            field=models.ImageField(null=True, upload_to='movies/panner'),
        ),
    ]

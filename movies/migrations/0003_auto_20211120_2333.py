# Generated by Django 3.1.2 on 2021-11-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211120_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Cast'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cat',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Category'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201125_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasepermutation',
            name='nome',
            field=models.CharField(default='Dataset', max_length=255, verbose_name='nome'),
        ),
    ]

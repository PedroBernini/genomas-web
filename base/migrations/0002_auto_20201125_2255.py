# Generated by Django 3.1.3 on 2020-11-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databasepermutation',
            name='maximo_breakpoints',
            field=models.IntegerField(blank=True, null=True, verbose_name='maximo_breakpoints'),
        ),
        migrations.AlterField(
            model_name='databasepermutation',
            name='minimo_breakpoints',
            field=models.IntegerField(blank=True, null=True, verbose_name='minimo_breakpoints'),
        ),
    ]

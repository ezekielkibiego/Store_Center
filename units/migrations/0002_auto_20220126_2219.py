# Generated by Django 3.2.9 on 2022-01-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

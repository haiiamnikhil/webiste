# Generated by Django 3.0 on 2020-12-03 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20201203_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='metakeywords',
        ),
    ]
# Generated by Django 3.0 on 2020-12-03 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201203_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='metta',
            new_name='metadescription',
        ),
        migrations.AddField(
            model_name='blog',
            name='metakeywords',
            field=models.TextField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]

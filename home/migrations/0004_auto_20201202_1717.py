# Generated by Django 3.0 on 2020-12-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201202_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='metadescription',
            field=models.TextField(max_length=256),
        ),
    ]

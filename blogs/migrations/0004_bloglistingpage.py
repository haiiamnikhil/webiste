# Generated by Django 3.0 on 2020-12-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201126_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=256)),
                ('metadescription', models.TextField(max_length=256)),
                ('metakeywords', models.TextField(max_length=256)),
            ],
        ),
    ]

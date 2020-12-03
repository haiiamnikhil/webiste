# Generated by Django 3.0 on 2020-12-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DesignAndDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalMarking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GraphicsDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MobileAppDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OurPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteDesignandDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metatitle', models.TextField(max_length=60)),
                ('metadescription', models.TextField(max_length=250)),
                ('metakeywords', models.TextField(blank=True, max_length=256)),
            ],
        ),
    ]
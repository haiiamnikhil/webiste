# Generated by Django 3.0 on 2020-11-26 07:47

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Admin', max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcategory', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('blogimage', models.ImageField(upload_to='blogs/')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField()),
                ('metta', models.TextField(max_length=256)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Processing'), (2, 'Live')], default=0)),
                ('published', models.DateField()),
                ('author', models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to='blogs.Author')),
                ('selectcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogCategory')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]

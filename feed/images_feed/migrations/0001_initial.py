# Generated by Django 2.1.5 on 2019-01-13 19:09

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/lusine/projects/feed/feed/media'), upload_to='photos')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]

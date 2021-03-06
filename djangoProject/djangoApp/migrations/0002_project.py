# Generated by Django 4.0.5 on 2022-06-13 08:05

from django.db import migrations, models
import djangoApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('revision', models.PositiveIntegerField()),
                ('visibility', models.CharField(max_length=255)),
                ('lastUpdateTime', models.DateTimeField()),
            ],
            bases=(djangoApp.models.UrlModelMixin, models.Model),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-25 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_blog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 11, 24, 53, 43048, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='dsc',
            field=models.TextField(default=datetime.datetime(2021, 7, 25, 11, 25, 4, 421497, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='news',
            field=models.CharField(default=datetime.datetime(2021, 7, 25, 11, 25, 22, 854024, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 7, 25, 11, 25, 34, 324489, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blg',
            field=models.TextField(),
        ),
    ]
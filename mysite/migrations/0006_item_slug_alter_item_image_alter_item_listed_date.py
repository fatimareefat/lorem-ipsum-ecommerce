# Generated by Django 4.0.1 on 2022-01-26 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_item_price_alter_item_listed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 26, 19, 28, 42, 453729)),
        ),
    ]
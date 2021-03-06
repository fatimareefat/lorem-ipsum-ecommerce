# Generated by Django 4.0.1 on 2022-01-27 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_item_listed_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 14, 29, 56, 329145)),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 14, 29, 56, 329145)),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-26 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_alter_item_listed_date_alter_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 26, 19, 38, 42, 349652)),
        ),
    ]
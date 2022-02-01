# Generated by Django 4.0.1 on 2022-01-26 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_item_quantity_alter_item_listed_date_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 26, 20, 52, 17, 182774)),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 20, 52, 17, 183779)),
        ),
    ]

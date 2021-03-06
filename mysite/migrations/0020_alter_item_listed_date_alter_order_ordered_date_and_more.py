# Generated by Django 4.0.1 on 2022-01-31 16:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_alter_item_listed_date_alter_item_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 21, 44, 10, 140411)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 21, 44, 10, 140411)),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=datetime.datetime(2022, 1, 31, 16, 14, 31, 30419, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 21, 44, 10, 140411)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 21, 44, 10, 140411)),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-27 12:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_alter_item_listed_date_alter_order_ordered_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.customer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 17, 44, 5, 879833)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 17, 44, 5, 880834)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 17, 44, 5, 881834)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 27, 17, 44, 5, 881834)),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-26 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_alter_item_listed_date_alter_item_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='listed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 26, 21, 17, 37, 888499)),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]

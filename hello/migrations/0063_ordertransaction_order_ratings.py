# Generated by Django 4.2 on 2023-09-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0062_womenshoefeatures_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertransaction',
            name='order_ratings',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, verbose_name='Order Ratings'),
            preserve_default=False,
        ),
    ]

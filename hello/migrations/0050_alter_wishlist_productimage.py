# Generated by Django 4.2 on 2023-08-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0049_alter_wishlist_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='productImage',
            field=models.URLField(max_length=255),
        ),
    ]

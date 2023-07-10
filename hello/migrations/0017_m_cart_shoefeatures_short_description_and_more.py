# Generated by Django 4.2 on 2023-07-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0016_womenshoefeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='shoefeatures',
            name='short_description',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='womenshoefeatures',
            name='short_description',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoefeatures',
            name='productName',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

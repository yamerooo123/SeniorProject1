# Generated by Django 4.2 on 2023-07-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0031_alter_ordertransaction_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoefeatures',
            name='maincolor',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='shoefeatures',
            name='subcolor',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='shoefeatures',
            name='subcolor2',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='womenshoefeatures',
            name='maincolor',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='womenshoefeatures',
            name='subcolor',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='womenshoefeatures',
            name='subcolor2',
            field=models.CharField(default='Black', max_length=255),
        ),
    ]

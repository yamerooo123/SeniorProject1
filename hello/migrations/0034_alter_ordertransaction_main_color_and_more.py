# Generated by Django 4.2 on 2023-07-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0033_ordertransaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertransaction',
            name='main_color',
            field=models.CharField(default='Black', max_length=255),
        ),
        migrations.AlterField(
            model_name='ordertransaction',
            name='status',
            field=models.CharField(default='Paid', max_length=255),
        ),
        migrations.AlterField(
            model_name='ordertransaction',
            name='sub_color',
            field=models.CharField(default='Black', max_length=255),
        ),
    ]

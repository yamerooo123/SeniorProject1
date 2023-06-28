from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_userprofile_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type1', models.CharField(max_length=255)),
                ('type2', models.CharField(max_length=255)),
                ('maincolor', models.CharField(max_length=255)),
                ('subcolor1', models.CharField(max_length=255)),
                ('subcolor2', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)), 
                ('brand', models.CharField(max_length=255)),
            ],
        ),
    ]

 
# Generated by Django 3.2.3 on 2021-06-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=50),
        ),
    ]

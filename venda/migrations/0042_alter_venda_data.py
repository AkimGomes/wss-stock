# Generated by Django 4.2 on 2023-10-08 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0041_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 15, 12, 49, 667717)),
        ),
    ]

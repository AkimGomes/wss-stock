# Generated by Django 4.2 on 2023-05-30 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venda", "0025_alter_venda_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venda",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 29, 21, 49, 35, 860585)
            ),
        ),
    ]

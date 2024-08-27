# Generated by Django 4.2 on 2023-05-19 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venda", "0019_alter_venda_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venda",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 19, 14, 56, 35, 505418)
            ),
        ),
        migrations.AlterField(
            model_name="venda",
            name="preco_total",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]

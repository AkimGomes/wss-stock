# Generated by Django 4.2 on 2023-10-17 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venda", "0059_alter_venda_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venda",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 17, 17, 20, 38, 905909)
            ),
        ),
    ]

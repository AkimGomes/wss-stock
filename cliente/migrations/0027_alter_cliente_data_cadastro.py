# Generated by Django 4.2.15 on 2024-08-26 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0026_alter_cliente_data_cadastro_alter_cliente_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="data_cadastro",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 8, 26, 14, 10, 7, 159513)
            ),
        ),
    ]

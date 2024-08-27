# Generated by Django 4.2 on 2023-05-30 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0006_alter_cliente_data_cadastro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="cpf",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="data_cadastro",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 5, 29, 21, 57, 37, 141740)
            ),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="nome",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="telefone_1",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

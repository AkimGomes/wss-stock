# Generated by Django 4.2 on 2023-05-30 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_cliente_cpf_alter_cliente_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 21, 52, 20, 200920)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone_1',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

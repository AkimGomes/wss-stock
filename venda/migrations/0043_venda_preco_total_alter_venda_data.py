# Generated by Django 4.2 on 2023-10-08 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0042_alter_venda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='preco_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 15, 16, 18, 866118)),
        ),
    ]

# Generated by Django 4.2 on 2023-10-08 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0034_remove_produtovenda_preco_alter_venda_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='preco_total',
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 15, 2, 54, 436658)),
        ),
    ]

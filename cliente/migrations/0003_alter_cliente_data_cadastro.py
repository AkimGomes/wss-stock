# Generated by Django 4.2 on 2023-05-30 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 21, 49, 35, 861062)),
        ),
    ]
# Generated by Django 4.2 on 2023-05-29 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 15, 24, 33, 782279)),
        ),
    ]

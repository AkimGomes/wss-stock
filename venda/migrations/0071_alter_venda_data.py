# Generated by Django 4.2.15 on 2024-08-26 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0070_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 26, 16, 39, 26, 551895)),
        ),
    ]

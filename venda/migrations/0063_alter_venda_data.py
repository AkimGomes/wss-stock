# Generated by Django 4.2 on 2024-08-08 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0062_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 15, 46, 15, 816012)),
        ),
    ]

# Generated by Django 4.2 on 2023-10-17 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0007_alter_orcamento_cliente_orcamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='data_orcamento',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 16, 48, 4, 454979)),
        ),
    ]

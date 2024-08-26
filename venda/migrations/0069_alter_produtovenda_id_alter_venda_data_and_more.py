# Generated by Django 4.2.15 on 2024-08-26 17:05

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0068_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtovenda',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 26, 14, 5, 14, 61801)),
        ),
        migrations.AlterField(
            model_name='venda',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.15 on 2024-08-26 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0023_alter_orcamento_data_orcamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='data_orcamento',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 26, 11, 58, 41, 931623)),
        ),
    ]
# Generated by Django 4.2 on 2023-10-17 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0015_alter_orcamento_data_orcamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='data_orcamento',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 17, 18, 57, 688423)),
        ),
    ]

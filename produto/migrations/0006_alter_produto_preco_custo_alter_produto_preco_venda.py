# Generated by Django 4.2 on 2023-04-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_preco_custo_alter_produto_preco_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_custo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_venda',
            field=models.FloatField(default=0.0),
        ),
    ]

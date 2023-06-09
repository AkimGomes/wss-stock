# Generated by Django 4.2 on 2023-04-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_alter_produto_preco_custo_alter_produto_preco_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_custo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_venda',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]

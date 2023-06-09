# Generated by Django 4.2 on 2023-05-18 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0010_alter_produto_preco_custo_alter_produto_preco_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('id_produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto', to='produto.produto')),
            ],
        ),
    ]

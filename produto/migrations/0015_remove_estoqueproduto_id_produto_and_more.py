# Generated by Django 4.2 on 2023-09-14 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0014_remove_produto_quantidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoqueproduto',
            name='id_produto',
        ),
        migrations.AddField(
            model_name='estoqueproduto',
            name='produto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estoque_produto', to='produto.produto'),
        ),
    ]

# Generated by Django 4.2.15 on 2024-08-26 14:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0015_remove_estoqueproduto_id_produto_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estoqueproduto",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]

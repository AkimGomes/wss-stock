# Generated by Django 4.2 on 2023-05-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0012_alter_estoqueproduto_id_produto"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="quantidade",
            field=models.IntegerField(default=0),
        ),
    ]

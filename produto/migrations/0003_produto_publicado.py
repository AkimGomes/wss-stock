# Generated by Django 4.2 on 2023-04-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_tipo_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]

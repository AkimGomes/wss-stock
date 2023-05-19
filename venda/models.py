from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

from produto.models import Produto


class ProdutoVenda(models.Model):
    produto_vendido = models.ForeignKey(
        to=Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="produto",
    )
    quantidade = models.IntegerField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False, default=0.0)

    def __str__(self):
        return f'{self.produto_vendido} - Quantidade: {self.quantidade}'


class Venda(models.Model):
    observacao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now(), blank=False)
    preco_total = models.FloatField(null=False, blank=False, default=0.0)
    produtos_venda = models.ManyToManyField(ProdutoVenda, blank=True)



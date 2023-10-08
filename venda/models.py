from datetime import datetime
from django.db import models
from django.db.models import Sum, F

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

    @property
    def preco(self):
        if self.produto_vendido and self.quantidade:
            return self.produto_vendido.preco_venda * self.quantidade
        return 0.0

    def __str__(self):
        return f'{self.produto_vendido} - Quantidade: {self.quantidade}'


class Venda(models.Model):
    observacao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now(), blank=False)
    preco_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    produtos_venda = models.ManyToManyField(ProdutoVenda, related_name="vendas")

    def __str__(self):
        return f'Venda - Data: {self.data}'



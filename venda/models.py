from datetime import datetime
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
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False, default=0.0)

    def __str__(self):
        return f'{self.produto_vendido} - Quantidade: {self.quantidade}'


class Venda(models.Model):
    observacao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now(), blank=False)
    preco_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Venda - Data: {self.data}'



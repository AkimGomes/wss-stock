from django.db import models


class Produto(models.Model):

    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    preco_custo = models.FloatField(null=False, blank=False, default=0.0)
    preco_venda = models.FloatField(null=False, blank=False, default=0.0)
    publicado = models.BooleanField(default=True)
    tipo_produto = models.CharField(max_length=50, null=False, blank=False)
    descricao_tipo = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome

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

    def get_quantidade_estoque(self):
        estoque_produto = EstoqueProduto.objects.filter(id_produto=self.id).first()
        return estoque_produto.quantidade if estoque_produto else 0


class EstoqueProduto(models.Model):

    id_produto = models.ForeignKey(
        to=Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="id_produto",
    )
    quantidade = models.IntegerField(null=False, blank=False)

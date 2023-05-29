from datetime import datetime

from django.db import models
from cliente.models import Cliente


class Orcamento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    cliente_orcamento = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True)
    data_orcamento = models.DateTimeField(default=datetime.now())
    valor_orcamento = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    ativo_inativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

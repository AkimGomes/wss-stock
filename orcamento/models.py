import uuid
from datetime import datetime

from django.db import models
from cliente.models import Cliente


class Orcamento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    cliente_orcamento = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    observacao = models.TextField(blank=True, null=True)
    data_orcamento = models.DateTimeField(default=datetime.now())
    valor_orcamento = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, null=True, blank=True)
    ativo_inativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

from datetime import datetime

from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)  # Considerando o formato XXX.XXX.XXX-XX
    telefone_1 = models.CharField(max_length=15, null=True, blank=True)  # Considerando o formato DDD + número (exemplo: 11 99999-9999)
    telefone_2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now())
    ativo_inativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

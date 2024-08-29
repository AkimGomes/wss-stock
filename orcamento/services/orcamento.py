from rest_framework import status
from rest_framework.response import Response
from orcamento.repo.orcamento import RepoOrcamentoLeitura, RepoOrcamentoEscrita


class OrcamentoService:
    orcamento_repositorio_leitura: RepoOrcamentoLeitura
    orcamento_repositorio_escrita: RepoOrcamentoEscrita

    def __init__(self):
        self.orcamento_repositorio_leitura = RepoOrcamentoLeitura()
        self.orcamento_repositorio_escrita = RepoOrcamentoEscrita()

    @staticmethod
    def criar_orcamento(orcamento_serializer):

        if orcamento_serializer.is_valid():
            orcamento_instance = orcamento_serializer.save()
            return orcamento_instance

        else:
            return Response(
                orcamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

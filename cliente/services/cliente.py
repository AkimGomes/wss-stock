from typing import Union

from rest_framework import status
from rest_framework.response import Response

from cliente.models import Cliente
from cliente.repo.cliente import RepoClienteLeitura


class ClienteService:
    cliente_repositorio_leitura: RepoClienteLeitura

    def __init__(self):
        self.cliente_repositorio_leitura = RepoClienteLeitura()

    def consultar_cliente_especifico_pelo_nome(
        self, nome: str
    ) -> Union[Cliente, Response]:
        cliente = self.cliente_repositorio_leitura.consultar_cliente_pelo_nome(
            nome=nome
        )
        if not cliente:
            return Response(
                {"message": "Nenhum cliente encontrado!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return cliente

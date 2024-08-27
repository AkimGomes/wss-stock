from typing import Union

from rest_framework import status
from rest_framework.response import Response

from produto.models import Produto
from produto.repo.produto import RepoProdutoLeitura


class ProdutoService:
    produto_repositorio: RepoProdutoLeitura

    def __init__(self):
        self.produto_repositorio = RepoProdutoLeitura()

    def consultar_produto_especifico_pelo_nome(self, nome: str) -> Union[Produto, Response]:
        produto = self.produto_repositorio.consultar_produto_pelo_nome(nome=nome)
        if not produto:
            return Response(
                {"message": "Nenhum produto encontrado!"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return produto


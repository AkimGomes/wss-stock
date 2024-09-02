from uuid import UUID

from django.db.models import QuerySet

from produto.models import Produto
from venda.models import Venda


class RepoVendaLeitura:

    @staticmethod
    def consultar_venda_pela_observacao(observacao: str) -> QuerySet[Venda]:
        venda = Venda.objects.filter(observacao__icontains=observacao)
        return venda

    @staticmethod
    def consultar_vendas_ordenada_pela_data_de_cadastro():
        vendas = Venda.objects.all().order_by("data")
        return vendas

    @staticmethod
    def consultar_venda_pelo_id(id: UUID) -> QuerySet[Venda]:
        venda = Venda.objects.get(pk=id)
        return venda


class RepoVendaEscrita:

    @staticmethod
    def deletar(venda: Venda):
        venda.delete()

    @staticmethod
    def salvar(venda: Venda):
        venda.save()

    @staticmethod
    def criar_venda(produto_vendido: Produto, quantidade: int) -> Venda:
        venda = Venda.objects.create(
            produto_vendido=produto_vendido,
            quantidade=quantidade,
        )
        return venda

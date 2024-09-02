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


class RepoVendaEscritaTeste:

    @staticmethod
    def criar_venda(observacao: str, preco_total: float) -> Venda:
        venda = Venda.objects.create(
            observacao=observacao,
            preco_total=preco_total,
        )
        return venda

    @staticmethod
    def deletar_todos_as_vendas():
        Venda.objects.all().delete()


class RepoVendaLeituraTeste:

    @staticmethod
    def consultar_unico_objeto_existente():
        venda = Venda.objects.get()
        return venda

    @staticmethod
    def contar_todos_as_vendas():
        quantidade_de_vendas = Venda.objects.count()
        return quantidade_de_vendas

from produto.models import Produto
from venda.models import ProdutoVenda


class RepoProdutoVendaLeitura:

    @staticmethod
    def consultar_venda_pela_observacao(observacao: str) -> QuerySet[ProdutoVenda]:
        venda = Venda.objects.filter(observacao__icontains=observacao)
        return venda


class RepoProdutoVendaEscrita:

    @staticmethod
    def criar_produto_venda(
        produto_vendido: Produto,
        quantidade: int,
    ) -> ProdutoVenda:
        produto_venda = ProdutoVenda.objects.create(
            produto_vendido=produto_vendido,
            quantidade=quantidade,
        )
        return produto_venda

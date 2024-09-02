from produto.models import Produto
from venda.models import ProdutoVenda


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

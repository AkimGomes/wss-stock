from uuid import UUID

from django.db.models import QuerySet

from produto.models import EstoqueProduto, Produto


class RepoEstoqueProdutoLeitura:

    @staticmethod
    def consultar_estoque_produto_pelo_produto(produto: Produto) -> EstoqueProduto:
        estoque_produto = EstoqueProduto.objects.get(produto=produto)
        return estoque_produto

    @staticmethod
    def consultar_todos_os_estoques_de_produtos() -> QuerySet[EstoqueProduto]:
        estoques_produtos = EstoqueProduto.objects.all().order_by("id")
        return estoques_produtos


class RepoEstoqueProdutoEscrita:

    @staticmethod
    def salvar(estoque_produto: EstoqueProduto):
        estoque_produto.save()

    @staticmethod
    def criar_estoque_de_produto(produto: Produto, quantidade: int) -> EstoqueProduto:
        estoque_produto = EstoqueProduto.objects.create(
            produto=produto, quantidade=quantidade
        )
        return estoque_produto


class RepoEstoqueProdutoLeituraTeste:

    @staticmethod
    def consultar_estoque_de_produto(produto: Produto) -> EstoqueProduto:
        estoque_produto = EstoqueProduto.objects.get(produto=produto)
        return estoque_produto


class RepoEstoqueProdutoEscritaTeste:

    @staticmethod
    def deletar_todos_os_estoques():
        EstoqueProduto.objects.all().delete()

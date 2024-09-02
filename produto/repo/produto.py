from uuid import UUID

from django.db.models import QuerySet

from produto.models import Produto


class RepoProdutoLeitura:

    @staticmethod
    def consultar_produto_pelo_id(id: UUID) -> Produto:
        produto = Produto.objects.get(pk=id)
        return produto

    @staticmethod
    def consultar_todos_os_produtos() -> QuerySet[Produto]:
        produtos = Produto.objects.all()
        return produtos

    @staticmethod
    def consultar_produto_pelo_nome(nome: str) -> QuerySet[Produto]:
        produto = Produto.objects.filter(nome__icontains=nome)
        return produto


class RepoProdutoEscritaTeste:

    @staticmethod
    def deletar_todos_os_produtos():
        Produto.objects.all().delete()

    @staticmethod
    def criar_produto(
        nome: str,
        descricao: str,
        preco_custo: float,
        preco_venda: float,
        tipo_produto: str,
        descricao_tipo: str,
    ) -> Produto:
        produto = Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco_custo=preco_custo,
            preco_venda=preco_venda,
            tipo_produto=tipo_produto,
            descricao_tipo=descricao_tipo,
        )
        return produto


class RepoProdutoLeituraTeste:

    @staticmethod
    def consultar_unico_objeto_existente():
        produto = Produto.objects.get()
        return produto

    @staticmethod
    def contar_todos_os_produtos():
        quantidade_de_produtos = Produto.objects.count()
        return quantidade_de_produtos

from produto.repo.estoque_produto import RepoEstoqueProdutoEscrita


class EstoqueProdutoService:
    estoque_de_produto_repositorio_escrita: RepoEstoqueProdutoEscrita

    def __init__(self):
        self.produto_repositorio = RepoEstoqueProdutoEscrita()

    def atualizar_estoque_de_produto_se_necessario(self, instance, quantidade: int):
        if quantidade is not None and quantidade != instance.estoque_produto.quantidade:
            instance.estoque_produto.quantidade = quantidade
            self.estoque_de_produto_repositorio_escrita.salvar(estoque_produto=instance.estoque_produto)


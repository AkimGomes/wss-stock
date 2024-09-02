from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from produto.models import EstoqueProduto, Produto
from produto.repo.estoque_produto import (
    RepoEstoqueProdutoLeitura,
    RepoEstoqueProdutoEscrita,
)
from produto.repo.produto import RepoProdutoLeitura
from venda.models import Venda, ProdutoVenda
from venda.repo.venda import RepoVendaLeitura, RepoVendaEscrita
from venda.serializers import VendaSerializer


class VendasViewSet(viewsets.ModelViewSet):
    """
    API de ProdutoVenda
    """

    permission_classes = (IsAuthenticated,)
    queryset = Venda.objects.all().order_by("data")
    queryset = RepoVendaLeitura.consultar_vendas_ordenada_pela_data_de_cadastro()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["data"]
    search_fields = ["data", "preco_total"]
    serializer_class = VendaSerializer

    def create(self, request, *args, **kwargs):
        venda_serializer = self.get_serializer(data=request.data)
        venda_serializer.is_valid(raise_exception=True)
        venda = venda_serializer.save()

        total_preco = 0

        produto_vendas = request.data.get("produtos_venda", [])
        venda.produtos_venda.clear()
        estoque_insuficiente = (
            False  # Variável para rastrear se há estoque insuficiente
        )

        for produto_data in produto_vendas:
            produto_id = produto_data.get("produto_vendido")
            quantidade = produto_data.get("quantidade")

            if produto_id and quantidade >= 0:
                produto = RepoProdutoLeitura.consultar_produto_pelo_id(id=produto_id)
                estoque_produto = (
                    RepoEstoqueProdutoLeitura.consultar_estoque_produto_pelo_produto(
                        produto=produto_id
                    )
                )

                if quantidade <= estoque_produto.quantidade:
                    produto_venda = RepoVendaEscrita.criar_venda(
                        produto_vendido=produto,
                        quantidade=quantidade,
                    )
                    venda.produtos_venda.add(produto_venda)

                    total_preco += produto_venda.preco

                    estoque_produto.quantidade -= quantidade
                    RepoEstoqueProdutoEscrita.salvar(estoque_produto=estoque_produto)
                else:
                    estoque_insuficiente = True  # Marque como estoque insuficiente

        if estoque_insuficiente:
            RepoVendaEscrita.deletar(venda=venda)
            return Response(
                {"detail": "Não é possível, produto com baixo estoque."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        venda.preco_total = total_preco
        RepoVendaEscrita.salvar(venda=venda)

        headers = self.get_success_headers(venda_serializer.data)
        return Response(
            venda_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["get"])
    def venda_info(self, request, pk=None):
        venda = self.get_object()

        venda_serializer = VendaSerializer(venda)

        data = {
            "venda": venda_serializer.data,
        }
        return Response(data, status=200)

    @action(detail=False, methods=["get"])
    def buscar(self, request):
        venda = self.request.query_params.get("buscar", None)

        if venda:
            vendas = RepoVendaLeitura.consultar_venda_pela_observacao(observacao=venda)

            if not vendas.exists():
                return Response(
                    {"message": "Nenhuma venda encontrada!"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        serializer = self.get_serializer(vendas, many=True)
        return Response(serializer.data)

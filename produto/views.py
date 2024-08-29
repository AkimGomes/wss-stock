from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from produto.models import EstoqueProduto
from produto.repo.estoque_produto import (
    RepoEstoqueProdutoLeitura,
    RepoEstoqueProdutoEscrita,
)
from produto.repo.produto import RepoProdutoLeitura
from produto.serializers import ProdutoSerializer, EstoqueProdutoSerializer
from produto.services.estoque_produto import EstoqueProdutoService
from produto.services.produto import ProdutoService

produto_service = ProdutoService()
estoque_produto_service = EstoqueProdutoService()


class ProdutosViewSet(viewsets.ModelViewSet):
    """
    API de Produtos
    """

    permission_classes = (IsAuthenticated,)
    queryset = RepoProdutoLeitura.consultar_todos_os_produtos()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "tipo_produto"]
    serializer_class = ProdutoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            produto_instance = serializer.save()

            quantidade = request.data.get("quantidade", 0)
            estoque_produto_instance = (
                RepoEstoqueProdutoEscrita.criar_estoque_de_produto(
                    produto=produto_instance, quantidade=quantidade
                )
            )

            response_data = serializer.data
            response_data["estoque_produto"] = EstoqueProdutoSerializer(
                estoque_produto_instance
            ).data

            response = Response(response_data, status=status.HTTP_201_CREATED)
            id = str(serializer.data.get("id"))
            response["Location"] = request.build_absolute_uri() + id
            return response

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        quantidade = request.data.get("quantidade")
        estoque_produto_service.atualizar_estoque_de_produto_se_necessario(
            instance=instance, quantidade=quantidade
        )

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def buscar(self, request):
        nome = self.request.query_params.get("buscar", None)

        if nome:
            produto = produto_service.consultar_produto_especifico_pelo_nome(nome=nome)

        serializer = self.get_serializer(produto, many=True)
        return Response(serializer.data)


class EstoqueProdutoViewSet(viewsets.ModelViewSet):
    """
    API de EstoqueProduto
    """

    permission_classes = (IsAuthenticated,)
    queryset = RepoEstoqueProdutoLeitura.consultar_todos_os_estoques_de_produtos()
    serializer_class = EstoqueProdutoSerializer

    @action(detail=True, methods=["get"])
    def estoque_produto_por_produto(self, request, pk=None):
        produto_id = self.kwargs.get("pk")

        estoque_produto = get_object_or_404(EstoqueProduto, produto=produto_id)

        # Serialize o objeto EstoqueProduto
        serializer = EstoqueProdutoSerializer(estoque_produto)

        # Retorne o JSON serializado
        return Response(serializer.data)
